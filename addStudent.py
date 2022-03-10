import sqlite3
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QListWidget, QMessageBox, QRadioButton
from PyQt5.QtCore import pyqtSlot
import sys


# has add remove student
class Student:
    def __init__(self):
        self.studID = "none"
        self.name = "none"

    def to_string(self):
        print("Student ID:", self.studID)
        print("Student Name:", self.name)


class Window(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.name_tb = QLabel(self)
        self.id_tb = QLabel(self)

        # Pop ups
        self.remove_student_id_error = QMessageBox(self)
        self.remove_student_id_error.setWindowTitle("ID Error")
        self.remove_student_id_error.setText("The ID you have entered is invalid. Please enter a valid ID")

        self.duplicate_entry = QMessageBox(self)
        self.duplicate_entry.setWindowTitle("Error")
        self.duplicate_entry.setText("Student ID already in use")

        # Add Text boxes to GUI
        self.student_id = QLineEdit(self)
        self.name = QLineEdit(self)

        # Add buttons to gui
        self.add_student = QPushButton(self)
        self.remove_student = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Add/Remove Student")
        self.setGeometry(50, 50, 800, 800)

        self.name_tb.setText('Students Name')
        self.name_tb.move(50, 50)
        self.name_tb.resize(180, 30)

        self.id_tb.setText('Student ID')
        self.id_tb.move(50, 250)
        self.id_tb.resize(180, 30)

        # Place text boxes in this section
        self.name.move(50, 80)
        self.name.resize(180, 40)

        self.student_id.move(50, 280)
        self.student_id.resize(180, 40)

        # button area
        self.add_student.setText("Add Student")
        self.add_student.move(500, 360)
        self.add_student.resize(180, 40)

        self.remove_student.setText("Remove Student")
        self.remove_student.move(500, 400)
        self.remove_student.resize(180, 40)
        
        self.add_student.clicked.connect(self.add_student_clicked)
        self.remove_student.clicked.connect(self.remove_student_clicked)

        # Showing Ui
        self.show()
    # add student connect
    def add_student_clicked(self):
        try:
            self.cursor.execute("""INSERT INTO Student (studID, studName) VALUES 
                (?,?)""", (self.student_id.text(), self.name.text()))
            query = f"""SELECT * FROM Student"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.duplicate_entry.exec()
            print(Exception, e)

    def remove_student_clicked(self):
        try:
            query = f"""SELECT EXISTS (SELECT * FROM Student WHERE studID = '{self.student_id.text()}') """
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 1:
                self.cursor.execute("""DELETE FROM Student WHERE (studID, studName) = 
                    (?,?)""", (self.student_id.text(), self.name.text()))
                query = f"""SELECT * FROM Student"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
            else:
                self.remove_student_id_error.exec()
        except Exception as e:
            print(Exception, e)
