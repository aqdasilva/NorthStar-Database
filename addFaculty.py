import sqlite3
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, \
    QListWidget, QMessageBox, QRadioButton
from PyQt5.QtCore import pyqtSlot
import sys


# has add remove faculty
class Faculty:
    def __init__(self):
        self.facultyID = "none"
        self.facultyName = "none"


    def to_string(self):
        print("Faculty ID:", self.facultyID)
        print("Faculty Name:", self.facultyName)



class Window(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.name_tb = QLabel(self)
        self.id_tb = QLabel(self)

        self.radio_desc = QLabel(self)

        # Pop ups
        self.faculty_in_use_error = QMessageBox(self)
        self.faculty_in_use_error.setWindowTitle("ERROR")
        self.faculty_in_use_error.setText("Cannot delete, students still enrolled in classes with professor")

        self.duplicate_faculty_entry = QMessageBox(self)
        self.duplicate_faculty_entry.setWindowTitle("Duplicate Entry Error")
        self.duplicate_faculty_entry.setText("ID already in use, please re-enter another faculty with a valid ID.")

        self.show_data = QMessageBox(self)
        self.show_data.setWindowTitle("Current Database")

        # Add Text boxes to GUI
        self.faculty_id = QLineEdit(self)
        self.name = QLineEdit(self)

        # Add buttons to gui
        self.add_faculty = QPushButton(self)
        self.remove_faculty = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Add/Remove Faculty")
        self.setGeometry(50, 50, 800, 800)

        self.name_tb.setText('Faculty Name')
        self.name_tb.move(50, 50)
        self.name_tb.resize(180, 30)

        self.id_tb.setText('Faculty ID')
        self.id_tb.move(50, 250)
        self.id_tb.resize(180, 30)

        # Place text boxes in this section
        self.name.move(50, 80)
        self.name.resize(180, 40)

        self.faculty_id.move(50, 280)
        self.faculty_id.resize(180, 40)

        # button area
        self.add_faculty.setText("Add Faculty")
        self.add_faculty.move(500, 360)
        self.add_faculty.resize(180, 40)

        self.remove_faculty.setText("Remove Faculty")
        self.remove_faculty.move(500, 400)
        self.remove_faculty.resize(180, 40)

        self.add_faculty.clicked.connect(self.add_faculty_clicked)
        self.remove_faculty.clicked.connect(self.remove_faculty_clicked)

        # Showing Ui
        self.show()

    # add faculty connect
    def add_faculty_clicked(self):
        try:
            self.cursor.execute("""INSERT INTO Faculty (facultyID, facultyName) VALUES 
                (?,?)""", (self.faculty_id.text(), self.name.text()))
            query = f"""SELECT * FROM Faculty"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.duplicate_faculty_entry.exec()
            print(Exception, e)

    def remove_faculty_clicked(self):
        try:
            query = f"""SELECT EXISTS (SELECT * FROM Enrollment WHERE facultyName = facultyName) """
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 0:
                self.cursor.execute("""DELETE FROM Faculty WHERE (facultyID, facultyName) = 
                    (?,?)""", (self.faculty_id.text(), self.name.text()))
                query = f"""SELECT * FROM Faculty"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
            else:
                self.faculty_in_use_error.exec()
        except Exception as e:
            print(Exception, e)
