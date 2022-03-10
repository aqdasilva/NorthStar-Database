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
        self.student_tb = QLabel(self)
        self.section_tb = QLabel(self)
        self.course_tb = QLabel(self)


        # Pop ups
        self.course_id_error = QMessageBox(self)
        self.course_id_error.setWindowTitle("ERROR")
        self.course_id_error.setText("Course Not Found. Please check Name/ID")

        # Add Text boxes to GUI
        self.student_id = QLineEdit(self)
        self.section_id = QLineEdit(self)
        self.course_id = QLineEdit(self)


        # Add buttons to gui
        self.add_to_Course = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Remove Flag")
        self.setGeometry(50, 50, 800, 800)

        self.student_tb.setText('Student ID')
        self.student_tb.move(50, 50)
        self.student_tb.resize(180, 30)

        self.section_tb.setText('Section ID')
        self.section_tb.move(50, 150)
        self.section_tb.resize(180, 30)

        self.course_tb.setText('Course ID')
        self.course_tb.move(50, 250)
        self.course_tb.resize(180, 30)



        # Place text boxes in this section
        self.student_id.move(50, 80)
        self.student_id.resize(180, 40)

        self.section_id.move(50, 180)
        self.section_id.resize(180, 40)

        self.course_id.move(50, 280)
        self.course_id.resize(180, 40)



        # button area
        self.add_to_Course.setText("Add to Course")
        self.add_to_Course.move(500, 360)
        self.add_to_Course.resize(180, 40)

        self.add_to_Course.clicked.connect(self.add_to_Course_clicked)

        # Showing Ui
        self.show()

    # add section
    def add_to_Course_clicked(self):
        studentID = self.student_id.text()
        sectionID = self.section_id.text()
        courseID = self.course_id.text()

        try:
            query = f"""SELECT EXISTS (SELECT * FROM Student WHERE studID ='{self.student_id.text()}')"""
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 1:
                self.cursor.execute(f"""INSERT INTO Enrollment (enrollmentID, studID, studName, courDesc,
                courID, sectID, facultyName, courCreds, flag) 
                VALUES (22,
                (SELECT studID from Student where studID = '{studentID}'),
                (SELECT studName from Student where studID = '{studentID}'),
                (SELECT courDesc from Course where courID = '{courseID}'),
                (SELECT courID from Section where sectID = '{sectionID}'),
                {sectionID},
                'Testing',
                (SELECT courCredits from Course where courID = '{courseID}'),
                1)
                """,)
                query = f"""SELECT * FROM Enrollment"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
            else:
                self.course_id_error.exec()
        # except Exception as e:
        # self.duplicate_entry.exec()
        except Exception as e:
            print(Exception, e)
