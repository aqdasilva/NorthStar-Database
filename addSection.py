import sqlite3
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, \
    QListWidget, QMessageBox, QRadioButton
from PyQt5.QtCore import pyqtSlot
import sys


# has edit student  & add
class Section:
    def __init__(self):
        self.courID = "none"
        self.sectID = "none"
        self.sectCap = "none"

    def to_string(self):
        print("Course ID:", self.courID)
        print("Section ID:", self.sectID)
        print("Section Capacity:", self.sectCap)


class Window(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.cour_id_tb = QLabel(self)
        self.sect_id_tb = QLabel(self)
        self.sect_cap_tb = QLabel(self)

        # Pop ups
        self.section_duplicate_entry = QMessageBox(self)
        self.section_duplicate_entry.setWindowTitle("Error")
        self.section_duplicate_entry.setText("Course ID entered does not exist")

        self.section_id_in_use = QMessageBox(self)
        self.section_id_in_use.setWindowTitle("Error")
        self.section_id_in_use.setText("Cannot delete, students still enrolled in classes with associated section")

        self.show_data = QMessageBox(self)
        self.show_data.setWindowTitle("Current Database")

        # Add Text boxes to GUI
        self.cour_id = QLineEdit(self)
        self.sect_id = QLineEdit(self)
        self.sect_cap = QLineEdit(self)

        # Add buttons to gui
        self.add_section = QPushButton(self)
        self.remove_section = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Add Section")
        self.setGeometry(50, 50, 800, 800)

        self.cour_id_tb.setText('Course ID')
        self.cour_id_tb.move(50, 50)
        self.cour_id_tb.resize(180, 30)

        self.sect_id_tb.setText('Section ID')
        self.sect_id_tb.move(50, 150)
        self.sect_id_tb.resize(180, 30)

        self.sect_cap_tb.setText('Section Capacity')
        self.sect_cap_tb.move(50, 250)
        self.sect_cap_tb.resize(180, 30)

        # Place text boxes in this section
        self.cour_id.move(50, 80)
        self.cour_id.resize(180, 40)

        self.sect_cap.move(50, 280)
        self.sect_cap.resize(180, 40)

        self.sect_id.move(50, 180)
        self.sect_id.resize(180, 40)

        # button area
        self.add_section.setText("Add Section")
        self.add_section.move(500, 360)
        self.add_section.resize(180, 40)

        self.remove_section.setText('Remove Section')
        self.remove_section.move(500, 320)
        self.remove_section.resize(180, 40)


        self.add_section.clicked.connect(self.add_section_clicked)
        self.remove_section.clicked.connect(self.remove_section_clicked)

        # Showing Ui
        self.show()

    # add section connection
    def add_section_clicked(self):
        try:
            self.cursor.execute("""INSERT INTO Section (sectID, courID, sectCap) VALUES 
                (?,?,?)""", (self.sect_id.text(), self.cour_id.text(), self.sect_cap.text()))
            query = f"""SELECT * FROM Section"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.section_duplicate_entry.exec()
            print(Exception, e)

    def remove_section_clicked(self):
        try:
            query = f"""SELECT EXISTS (SELECT * FROM Enrollment WHERE sectID = sectID) """
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 1:
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
                self.cursor.execute("""DELETE FROM Section WHERE (sectID, courID, sectCap) = 
                    (?,?,?)""", (self.sect_id.text(), self.cour_id.text(), self.sect_cap.text()))
                query = f"""SELECT * FROM Section"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
        except Exception as e:
            self.section_id_in_use.exec()
            print(Exception, e)
