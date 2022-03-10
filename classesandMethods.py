import sqlite3
from typing import List, Dict



class Student:
    def __init__(self):

        self.name = "none"
        self.id = 0

    def addStudent(self, name, id):
        # We need two buttons for the input of student
        # Lets call "Student Name" text box = studentName
        # Lets call "Student ID" text box = studentID

        new_student = Student()
        new_student.name = self.studentName.text()
        new_student.id = self.studentID.text()
        n = int("number of students: ")
        all_students = []
        for i in range(0, n):
            stud_name = ("Name of the student")


    def checkStudent(self, student_list: Dict, enroll_list: List):
        if len(enroll_list) > 0:
            for enroll in enroll_list:
                id = student_list[enroll.course_id].id

        if id != student_list[self.addStudent()].id:
            return True
        else:
            return False

    def deleteStudent(self, student_list: Dict):
        student_ID = int(input("Enter Student ID: "))
        statmt = "DELETE FROM 'students' WHERE Student.studID='{studentID}'"
        cur.execute(statmt, (student_ID))
        conn.commit()






class Course:
    def __init__(self):

        self.cid = 0
        self.cname = "none"
        self.limit = 30
        self.credit = 0

    def newCourse(self, cname, cid, limit, credit):

        new_course = Course()
        new_course.cname = self.name.text()
        new_course.cid = self.cid.text()
        new_course.limit = self.limit.text()

        def checkCourse(self, course_list: Dict, enroll_list: List):
            if len(enroll_list) > 0:
                for enroll in enroll_list:
                    id = course_list[enroll.course_id].id

            if id != course_list[self.addStudent()].id:
                return True
            else:
                return False


class Section:
    def __init__(self):
        self.sid = 0

        def newSection(self):
            new_section = Section()
            new_section.id = self.Section.id()


class Faculty:
    def __init__(self):
        self.fname = "none"
        self.fid = 0

    def newFaculty(self, fname, fid):
        new_Faculty = Course()
        new_Faculty.fname = self.fname.text()
        new_Faculty.id = self.fid.text()

        def checkCourse(self, staff_list: Dict, enroll_list: List):
            if len(enroll_list) > 0:
                for enroll in enroll_list:
                    id = staff_list[enroll.course_id].id

            if id != staff_list[self.addStudent()].id:
                return True
            else:
                return False

class functions:

    def newFaculty(self):
        # We need two buttons for the input of student
        # Lets call "Faculty Name" text box = facultyName
        # Lets call "Faculty ID" text box = facultyID
        new_faculty = Faculty()
        new_faculty.name = self.facultyName.text()
        new_faculty.id = self.facultyID.text()

    def newCourse(self):
        new_course = Course()
        new_course.name = self.courseName.text()
        new_course.id = self.courseID.text()
        new_course.limit = self.courseLimit.text()


class Enrollment:

    def __init__(self, cursor):
        self.cursor = cursor
        self.student_id = ''
        self.course_id = ''
        self.flag = 0

    #  This checks to see if the credits has exceeded the 12 threshold
    #  I have each class being 4 credits and therefore if it is over 3 classes, the last one
    #  will have the flag
    #  This should also be done with an SQL query like on the board, but to set the flag is going
    #  to be nearly identical.
    def check_credits(self, course_list: Dict, enroll_list: List):
        total_credits = 0
        if len(enroll_list) > 0:
            for enroll in enroll_list:
                total_credits += course_list[enroll.course_id].credits

        if total_credits + course_list[self.course_id].credits > 12:
            return True
        else:
            return False

    #  This will be replaced with SQL queries, but for now my return is acting like the INSERT
    def add_enrollment(self, stu_id, c_id, course_list: Dict, enroll_list: List):
        course = course_list[c_id]
        self.student_id = stu_id
        self.course_id = c_id

        if self.check_credits(course_list, enroll_list):
            self.flag = 1
        else:
            self.flag = 0

        # self.to_string()
        return self
