import sqlite3
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, \
    QListWidget, QMessageBox, QRadioButton
from PyQt5.QtCore import pyqtSlot
import sys


# has edit faculty
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

        # Pop ups
        self.faculty_id_error= QMessageBox(self)
        self.faculty_id_error.setWindowTitle("Error")
        self.faculty_id_error.setText("Employee ID not found.")


        # Add Text boxes to GUI
        self.facultyID = QLineEdit(self)
        self.facultyName = QLineEdit(self)

        # Add buttons to gui
        self.add_edit = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Edit Faculty")
        self.setGeometry(50, 50, 800, 800)

        self.name_tb.setText('Faculty Name')
        self.name_tb.move(50, 50)
        self.name_tb.resize(180, 30)

        self.id_tb.setText('Faculty ID')
        self.id_tb.move(50, 250)
        self.id_tb.resize(180, 30)

        # Place text boxes in this section
        self.facultyName.move(50, 80)
        self.facultyName.resize(180, 40)

        self.facultyID.move(50, 280)
        self.facultyID.resize(180, 40)

        # button area
        self.add_edit.setText("Edit")
        self.add_edit.move(500, 360)
        self.add_edit.resize(180, 40)

        self.add_edit.clicked.connect(self.add_edit_clicked)

        # Showing Ui
        self.show()

    # edit faculty connect
    def add_edit_clicked(self):
        try:
            query = f"""SELECT EXISTS (SELECT * FROM Faculty WHERE facultyID = '{self.facultyID.text()}') """
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 1:
                self.cursor.execute("""UPDATE Faculty SET (facultyName) =
                    (?) WHERE (facultyID) = (?)""", (self.facultyName.text(), self.facultyID.text()))
                query = f"""SELECT * FROM Faculty"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
            else:
                self.faculty_id_error.exec()
        # except Exception as e:
        # self.duplicate_entry.exec()
        except Exception as e:
            print(Exception, e)
