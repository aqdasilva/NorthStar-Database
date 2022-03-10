import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox
import pandas as pd
import sys


class Window(QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()
        # Database tools
        self.cursor = curs
        self.connection = conn
        self.window = Add_Student_to_Course(self.connection, self.cursor)
        self.window1 = StudentRegistration(self.connection, self.cursor)
        self.window2 = Add_RemoveStudent(self.connection, self.cursor)
        self.window3 = Edit_Student(self.connection, self.cursor)
        self.window4 = Add_Faculty(self.connection, self.cursor)
        self.window5 = Edit_Faculty(self.connection, self.cursor)
        self.window6 = Add_Remove_Course(self.connection, self.cursor)
        self.window7 = Edit_Course(self.connection, self.cursor)
        self.window8 = Add_Section(self.connection, self.cursor)
        self.window9 = Remove_Flag(self.connection, self.cursor)
        self.window.hide()
        self.window1.hide()
        self.window2.hide()
        self.window3.hide()
        self.window4.hide()
        self.window5.hide()
        self.window6.hide()
        self.window7.hide()
        self.window8.hide()
        self.window9.hide()

        # Labels
        self.title = 'Database'

        # Menu Buttons
        self.test_button1 = QPushButton(self)
        self.test_button = QPushButton(self)
        self.test_button2 = QPushButton(self)
        self.test_button3 = QPushButton(self)
        self.test_button4 = QPushButton(self)
        self.test_button5 = QPushButton(self)
        self.test_button6 = QPushButton(self)
        self.test_button7 = QPushButton(self)
        self.test_button8 = QPushButton(self)
        self.test_button9 = QPushButton(self)

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("North Star College for the Arts")
        self.setGeometry(50, 50, 800, 800)

        self.test_button1.resize(180, 30)
        self.test_button1.move(50, 50)
        self.test_button1.setText('Add Student to Course')
        self.test_button1.clicked.connect(self.test_button1_connection)

        self.test_button.resize(180, 30)
        self.test_button.move(50, 100)
        self.test_button.setText('Print Student Info')
        self.test_button.clicked.connect(self.test_button_connection)

        self.test_button2.resize(180, 30)
        self.test_button2.move(50, 150)
        self.test_button2.setText('Add/Remove Student')
        self.test_button2.clicked.connect(self.test_button2_connection)

        self.test_button3.resize(180, 30)
        self.test_button3.move(50, 200)
        self.test_button3.setText('Edit Student')
        self.test_button3.clicked.connect(self.test_button3_connection)

        self.test_button4.resize(180, 30)
        self.test_button4.move(50, 250)
        self.test_button4.setText('Add/Remove Faculty')
        self.test_button4.clicked.connect(self.test_button4_connection)

        self.test_button5.resize(180, 30)
        self.test_button5.move(50, 300)
        self.test_button5.setText('Edit Faculty')
        self.test_button5.clicked.connect(self.test_button5_connection)

        self.test_button6.resize(180, 30)
        self.test_button6.move(50, 350)
        self.test_button6.setText('Add/Remove Course')
        self.test_button6.clicked.connect(self.test_button6_connection)

        self.test_button7.resize(180, 30)
        self.test_button7.move(50, 400)
        self.test_button7.setText('Edit Course')
        self.test_button7.clicked.connect(self.test_button7_connection)

        self.test_button8.resize(180, 30)
        self.test_button8.move(50, 450)
        self.test_button8.setText('Add/Remove Section')
        self.test_button8.clicked.connect(self.test_button8_connection)

        self.test_button9.resize(180, 30)
        self.test_button9.move(50, 500)
        self.test_button9.setText('Remove a Flag')
        self.test_button9.clicked.connect(self.test_button9_connection)

        # Showing Ui
        self.show()

    def test_button1_connection(self, checked):
        self.window.show()

    def test_button_connection(self, checked):
        self.window1.show()

    def test_button2_connection(self, checked):
        self.window2.show()

    def test_button3_connection(self, checked):
        self.window3.show()

    def test_button4_connection(self, checked):
        self.window4.show()

    def test_button5_connection(self, checked):
        self.window5.show()

    def test_button6_connection(self, checked):
        self.window6.show()

    def test_button7_connection(self, checked):
        self.window7.show()

    def test_button8_connection(self, checked):
        self.window8.show()

    def test_button9_connection(self, checked):
        self.window9.show()


class Add_Student_to_Course(QMainWindow):
    counter = 20

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
        self.checkingCredits = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Add Student to Course")
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

        self.checkingCredits.setText("Check Credits")
        self.checkingCredits.move(500, 460)
        self.checkingCredits.resize(180, 40)

        self.checkingCredits.clicked.connect(self.check_credits)
        self.add_to_Course.clicked.connect(self.add_to_Course_clicked)

        # Showing Ui
        self.show()

    # add section

    def check_credits(self):

        total_credits = 0
        try:
            '''self.cursor.execute(f"""SELECT courCredits
                                FROM Course
                                WHERE Course.courID = ?"""
                                , (self.course_id.text(),))'''

            self.cursor.execute(f"""SELECT SUM(E.courCreds)
                                    FROM Enrollment E
                                    WHERE E.studID = ?


                                    """, (self.student_id.text(),))

            df = self.cursor.fetchone()
            theValue = int(df[0])

            print(theValue)

            if theValue > 12:
                return True
            else:
                return False


        except Exception as e:
            print(Exception, e)

    '''def check_cap(self):

        total_credits = 0
        try:

            self.cursor.execute(f"""SELECT COUNT(*)
                                     FROM Enrollment
                                    WHERE Enrollment.studID = ?"""
                                , (self.student_id.text(),))

            df = self.cursor.fetchone()
            theValue = int(df[0])

            if theValue - 1 < 0:
                return True
            else:
                return False


        except Exception as e:
            print(Exception, e)'''

    def add_to_Course_clicked(self, counter=None):
        studentID = self.student_id.text()
        sectionID = self.section_id.text()
        courseID = self.course_id.text()
        counter = counter + 1
        try:

            query = f"""SELECT EXISTS (SELECT * FROM Student WHERE studID ='{self.student_id.text()}')"""
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            otherFlag = Add_Student_to_Course.check_credits(self)
            if flag == 1:
                self.cursor.execute(f"""INSERT INTO Enrollment (studID, studName, courDesc,
                courID, sectID, facultyName, courCreds, flag) 
                VALUES (
                (SELECT studID from Student where studID = '{studentID}'),
                (SELECT studName from Student where studID = '{studentID}'),
                (SELECT courDesc from Course where courID = '{courseID}'),
                (SELECT courID from Section where sectID = '{sectionID}'),
                {sectionID},
                (SELECT facultyName from Section where sectID = '{sectionID}'),
                (SELECT courCredits from Course where courID = '{courseID}'),
                0)
                """, )
                query = f"""SELECT * FROM Enrollment"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
                print(counter)

            else:
                self.course_id_error.exec()
        # except Exception as e:
        # self.duplicate_entry.exec()
        except Exception as e:
            print(Exception, e)


class StudentRegistration(QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'

        self.studentID_Label = QLabel(self)

        self.studentID = QLineEdit(self)

        self.test_button = QPushButton(self)

        # Pop ups
        self.id_error = QMessageBox(self)
        self.id_error.setWindowTitle("ID Error")
        self.id_error.setText("ID is invalid, enter valid ID")

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Print Student Registration")
        self.setGeometry(50, 50, 800, 800)

        self.studentID_Label.setText("Enter student ID")
        self.studentID_Label.resize(180, 30)
        self.studentID_Label.move(50, 10)

        self.studentID.move(50, 50)
        self.studentID.resize(200, 40)

        self.test_button.resize(180, 30)
        self.test_button.move(50, 100)
        self.test_button.setText('Select Information')
        self.test_button.clicked.connect(self.test_button_connection)
        # Showing Ui
        self.show()

    def test_button_connection(self):
        studentID = self.studentID.text()
        # selects this exist provide boolean value
        try:
            query = f"""SELECT EXISTS(SELECT 1 FROM Enrollment WHERE studID = '{studentID}')"""
            flag = self.cursor.execute(query).fetchall()[0][0]
            if flag == 1:
                # query = f"""SELECT * FROM{table}"""
                # next line is joins of all database elements, this is query to print registration information
                # instead of taking a student ID
                query = f"""SELECT Enrollment.studID, Enrollment.studname, Enrollment.courDesc, Enrollment.courID, 
                    Enrollment.sectID, Enrollment.facultyName, Enrollment.courCreds, flag FROM
                    Enrollment INNER JOIN Student S on S.studID = Enrollment.studID
                    INNER JOIN SECTION Sec on Sec.sectID = Enrollment.sectID
                    INNER JOIN Course C on Sec.courID = C.courID WHERE Enrollment.studID = '{studentID}'"""
                self.cursor.execute(query)
                # WHERE selects from table a specific parameter

                df = pd.DataFrame.from_records(self.cursor.fetchall())

                print(df)  # print to window figure out and google it

            else:
                self.id_error.exec()
        except Exception as e:
            print(Exception, e)


class Add_RemoveStudent(QMainWindow):
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


class Edit_Student(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.name_tb = QLabel(self)
        self.id_tb = QLabel(self)

        # Pop ups
        self.id_error = QMessageBox(self)
        self.id_error.setWindowTitle("ERROR")
        self.id_error.setText("Student ID entered was not found")

        # Add Text boxes to GUI
        self.student_id = QLineEdit(self)
        self.name = QLineEdit(self)

        # Add buttons to gui
        self.add_edit = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Edit Student")
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
        self.add_edit.setText("Edit")
        self.add_edit.move(500, 360)
        self.add_edit.resize(180, 40)

        self.add_edit.clicked.connect(self.add_edit_clicked)

        # Showing Ui
        self.show()

    # edit student connect
    def add_edit_clicked(self):
        try:
            query = f"""SELECT EXISTS (SELECT * FROM Student WHERE studID = '{self.student_id.text()}') """
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            if flag == 1:
                self.cursor.execute("""UPDATE Student SET (studName) =
                    (?) WHERE (studID) = (?)""", (self.name.text(), self.student_id.text()))
                query = f"""SELECT * FROM Student"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
            else:
                self.id_error.exec()
        # except Exception as e:
        # self.duplicate_entry.exec()
        except Exception as e:
            print(Exception, e)


class Add_Faculty(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.name_tb = QLabel(self)
        self.id_tb = QLabel(self)

        # Pop ups
        self.faculty_in_use_error = QMessageBox(self)
        self.faculty_in_use_error.setWindowTitle("Error")
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
            self.connection.commit()
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


class Edit_Faculty(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.name_tb = QLabel(self)
        self.id_tb = QLabel(self)

        # Pop ups
        self.faculty_id_error = QMessageBox(self)
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


class Add_Remove_Course(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.cour_id_tb = QLabel(self)
        self.cour_desc_tb = QLabel(self)
        self.cour_credits_tb = QLabel(self)

        # Pop ups
        self.course_duplicate_entry = QMessageBox(self)
        self.course_duplicate_entry.setWindowTitle("Error")
        self.course_duplicate_entry.setText("Course ID already exist")

        self.incorrect_entry = QMessageBox(self)
        self.incorrect_entry.setWindowTitle("Error")
        self.incorrect_entry.setText("Course ID does not exist")

        # Add Text boxes to GUI
        self.cour_id = QLineEdit(self)
        self.cour_desc = QLineEdit(self)
        self.cour_credits = QLineEdit(self)

        # Add buttons to gui
        self.add_course = QPushButton(self)
        self.remove_course = QPushButton(self)

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Add Course")
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

        self.cour_credits.move(50, 280)
        self.cour_credits.resize(180, 40)

        self.cour_desc.move(50, 180)
        self.cour_desc.resize(180, 40)

        # button area
        self.add_course.setText("Add Course")
        self.add_course.move(500, 360)
        self.add_course.resize(180, 40)

        self.remove_course.setText('Remove Course')
        self.remove_course.move(500, 320)
        self.remove_course.resize(180, 40)

        self.add_course.clicked.connect(self.add_course_clicked)
        self.remove_course.clicked.connect(self.remove_course_clicked)

        # Showing Ui
        self.show()

    # add section
    def add_course_clicked(self):
        try:
            query = f"""SELECT * FROM Course"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
            self.cursor.execute("""INSERT INTO Course (courID, courDesc, courCredits) VALUES 
                (?,?,?)""", (self.cour_id.text(), self.cour_desc.text(), self.cour_credits.text()))
            self.connection.commit()
            query = f"""SELECT * FROM Course"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.course_duplicate_entry.exec()
            print(Exception, e)

    def remove_course_clicked(self):
        try:
            query = f"""SELECT * FROM Course"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
            self.cursor.execute("""DELETE FROM Course WHERE (courID, courDesc, courCredits) =
                (?,?,?)""", (self.cour_id.text(), self.cour_desc.text(), self.cour_credits.text()))
            self.connection.commit()
            query = f"""SELECT * FROM Course"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.incorrect_entry.exec()
            print(Exception, e)


class Edit_Course(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database'
        self.cour_id_tb = QLabel(self)
        self.cour_desc_tb = QLabel(self)

        # Pop ups
        self.course_id_error = QMessageBox(self)
        self.course_id_error.setWindowTitle("ERROR")
        self.course_id_error.setText("Course Not Found. Please check Name/ID")

        # Add Text boxes to GUI
        self.cour_id = QLineEdit(self)
        self.cour_desc = QLineEdit(self)

        # Add buttons to gui
        self.edit_course = QPushButton(self)

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

        # Place text boxes in this section
        self.cour_id.move(50, 80)
        self.cour_id.resize(180, 40)

        self.cour_desc.move(50, 180)
        self.cour_desc.resize(180, 40)

        # button area
        self.edit_course.setText("Edit")
        self.edit_course.move(500, 360)
        self.edit_course.resize(180, 40)

        self.edit_course.clicked.connect(self.edit_course_clicked)

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
        except Exception as e:
            print(Exception, e)


class Add_Section(QMainWindow):
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
            self.connection.commit()
            query = f"""SELECT * FROM Section"""
            self.cursor.execute(query)
            df = pd.DataFrame.from_records(self.cursor.fetchall())
            print(df)
        except Exception as e:
            self.section_duplicate_entry.exec()
            print(Exception, e)

    def remove_section_clicked(self):
        try:
            query = f"""SELECT EXISTS(SELECT * FROM Enrollment WHERE sectID = '{self.sect_id_tb.text()}')"""
            print("GOT HERE")
            self.cursor.execute(query)
            flag = self.cursor.fetchone()[0]
            print(flag)
            if flag == 1:
                query = f"""DELETE FROM Section WHERE sectID = 
                     '{self.sect_id_tb.text()}'"""
                self.cursor.execute(query)
                query = f"""SELECT * FROM Section"""
                self.cursor.execute(query)
                df = pd.DataFrame.from_records(self.cursor.fetchall())
                print(df)
            else:
                print("THIS ERROR")
                self.section_id_in_use.exec()
        except Exception as e:
            self.section_id_in_use.exec()
            print(Exception, e)


class Remove_Flag(QMainWindow):

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
