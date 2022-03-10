import addStudent
import addFaculty
import addSection
import guiWindow
import sys
import sqlite3 as sql


def main():
    # Main database stuff here
    conn = sql.connect('north_star_practice_db.db')
    cursor = conn.cursor()
    # get_info(cursor, id) # May want to consider including this in GUI

    app = addSection.QApplication(sys.argv)
    ex = addSection.Window(conn, cursor)


    ex.isHidden()
    sys.exit(app.exec_())

main()