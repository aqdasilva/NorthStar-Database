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
        self.flag_tb = QLabel(self)


        # Pop ups
        self.course_id_error = QMessageBox(self)
        self.course_id_error.setWindowTitle("ERROR")
        self.course_id_error.setText("Course Not Found. Please check Name/ID")

        # Add Text boxes to GUI
        self.student_id = QLineEdit(self)


        # Add buttons to gui
        self.remove_flag = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Remove Flag")
        self.setGeometry(50, 50, 800, 800)

        self.flag_tb.setText('Student ID')
        self.flag_tb.move(50, 50)
        self.flag_tb.resize(180, 30)



        # Place text boxes in this section
        self.student_id.move(50, 80)
        self.student_id.resize(180, 40)



        # button area
        self.remove_flag.setText("Remove Flag")
        self.remove_flag.move(500, 360)
        self.remove_flag.resize(180, 40)

        self.remove_flag.clicked.connect(self.remove_flag_clicked)

        # Showing Ui
        self.show()

    # add section
    def remove_flag_clicked(self):
        try:
            query = f"""SELECT EXISTS (SELECT * FROM Enrollment WHERE studID ='{self.student_id.text()}')"""
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 1:
                self.cursor.execute("""UPDATE Enrollment SET (flag) =
                 (?) WHERE (studID) = (?)""", (0, self.student_id.text()))
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
