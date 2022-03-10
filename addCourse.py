import sqlite3
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, \
    QListWidget, QMessageBox, QRadioButton
from PyQt5.QtCore import pyqtSlot
import sys


# has edit course
class Course:
    def __init__(self):
        self.courID = "none"
        self.courDesc = "none"
        self.courCredits = "none"

    def to_string(self):
        print("Course ID:", self.courID)
        print("Course Description:", self.courDesc)
        print("Course Credits:", self.courCredits)


class Window(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.cour_id_tb = QLabel(self)
        self.cour_desc_tb = QLabel(self)
        self.cour_credits_tb = QLabel(self)

        # Pop ups
        self.course_id_error = QMessageBox(self)
        self.course_id_error.setWindowTitle("ERROR")
        self.course_id_error.setText("Course Not Found. Please check Name/ID")

        # Add Text boxes to GUI
        self.cour_id = QLineEdit(self)
        self.cour_desc = QLineEdit(self)
        self.cour_credits = QLineEdit(self)

        # Add buttons to gui
        self.edit_course = QPushButton(self)
        self.add_course = QPushButton(self)
        self.remove_course = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Edit Course")
        self.setGeometry(50, 50, 800, 800)

        self.cour_id_tb.setText('Course ID')
        self.cour_id_tb.move(50, 50)
        self.cour_id_tb.resize(180, 30)

        self.cour_desc_tb.setText('Course Description')
        self.cour_desc_tb.move(50, 150)
        self.cour_desc_tb.resize(180, 30)

        self.cour_credits_tb.setText('Course Credits')
        self.cour_credits_tb.move(50, 250)
        self.cour_credits_tb.resize(180, 30)

        # Place text boxes in this section
        self.cour_id.move(50, 80)
        self.cour_id.resize(180, 40)

        self.cour_desc.move(50, 180)
        self.cour_desc.resize(180, 40)

        self.cour_credits.move(50, 280)
        self.cour_credits.resize(180, 40)

        # button area
        self.edit_course.setText("Edit")
        self.edit_course.move(500, 360)
        self.edit_course.resize(180, 40)

        self.add_course.setText("Add")
        self.add_course.move(500, 400)
        self.add_course.resize(180, 40)

        self.remove_course.setText("Remove")
        self.remove_course.move(500, 440)
        self.remove_course.resize(180, 40)

        self.edit_course.clicked.connect(self.edit_course_clicked)
        self.add_course.clicked.connect(self.add_course_clicked)
        self.remove_course.clicked.connect(self.remove_course_clicked)

        # Showing Ui
        self.show()

    # add section
    def edit_course_clicked(self):
        try:
            query = f"""SELECT EXISTS (SELECT * FROM Course WHERE courID ='{self.cour_id.text()}')"""
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 1:
                self.cursor.execute("""UPDATE Course SET (courDesc) =
                 (?) WHERE (courID) = (?)""", (self.cour_desc.text(), self.cour_id.text()))
                query = f"""SELECT * FROM Course"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
            else:
                self.course_id_error.exec()
        # except Exception as e:
        # self.duplicate_entry.exec()
        except Exception as e:
            print(Exception, e)

    def add_course_clicked(self):
        try:
            self.cursor.execute("""INSERT INTO Course (courID, courDesc, courCredits) VALUES 
                (?,?,?)""", (self.cour_id.text(), self.cour_desc.text(), self.cour_credits.text()))
            query = f"""SELECT * FROM Course"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.duplicate_faculty_entry.exec()
            print(Exception, e)

    def remove_course_clicked(self):
        try:
            self.cursor.execute("""DELETE FROM Course WHERE (courID, courDesc, courCredits) =
                (?,?,?)""", (self.cour_id.text(), self.cour_desc.text(), self.cour_credits.text()))
            query = f"""SELECT * FROM Course"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.duplicate_faculty_entry.exec()
            print(Exception, e)
