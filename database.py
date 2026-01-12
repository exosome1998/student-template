import sqlite3
import os

DATABASE = "student_portal.db"

def init_db():
    """Initialize the database with tables and sample data"""
    if os.path.exists(DATABASE):
        return

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # Create users table
    cur.execute('''
        CREATE TABLE users (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            phone TEXT
        )
    ''')

    # Create grades table
    cur.execute('''
        CREATE TABLE grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            subject TEXT,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES users(student_id)
        )
    ''')

    # Create assignments table
    cur.execute('''
        CREATE TABLE assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            assignment_name TEXT,
            link TEXT,
            FOREIGN KEY (student_id) REFERENCES users(student_id)
        )
    ''')

    # Create announcements table
    cur.execute('''
        CREATE TABLE announcements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            date TEXT
        )
    ''')

    # Create comments table
    cur.execute('''
        CREATE TABLE comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            comment TEXT,
            date TEXT,
            FOREIGN KEY (student_id) REFERENCES users(student_id)
        )
    ''')

    # Insert sample users (VULNERABILITY: Plain text passwords)
    cur.execute("INSERT INTO users VALUES ('S12345', 'Alice Johnson', 'password123', 'alice@school.edu', '0412345678')")
    cur.execute("INSERT INTO users VALUES ('S12346', 'Bob Smith', 'qwerty', 'bob@school.edu', '0423456789')")
    cur.execute("INSERT INTO users VALUES ('S12347', 'Charlie Brown', 'abc123', 'charlie@school.edu', '0434567890')")

    # Insert sample grades
    cur.execute("INSERT INTO grades (student_id, subject, grade) VALUES ('S12345', 'Mathematics', 'A')")
    cur.execute("INSERT INTO grades (student_id, subject, grade) VALUES ('S12345', 'English', 'B+')")
    cur.execute("INSERT INTO grades (student_id, subject, grade) VALUES ('S12346', 'Mathematics', 'B')")
    cur.execute("INSERT INTO grades (student_id, subject, grade) VALUES ('S12346', 'English', 'A-')")

    # Insert sample announcements
    cur.execute("INSERT INTO announcements (title, content, date) VALUES ('Welcome Back', 'Welcome to the new semester!', '2026-01-15')")
    cur.execute("INSERT INTO announcements (title, content, date) VALUES ('Exam Schedule', 'Final exams start next week.', '2026-01-16')")

    conn.commit()
    conn.close()


# VULNERABILITY: SQL Injection in login
def checkLogin(student_id, password):
    """Check if login credentials are valid"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    query = f"SELECT * FROM users WHERE student_id = '{student_id}' AND password = '{password}'"
    cur.execute(query)

    user = cur.fetchone()
    conn.close()

    return user


# VULNERABILITY: SQL Injection in grade lookup
def getGrades(student_id):
    """Get grades for a student"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    query = f"SELECT * FROM grades WHERE student_id = '{student_id}'"
    cur.execute(query)

    grades = cur.fetchall()
    conn.close()

    return grades


# VULNERABILITY: SQL Injection in assignment submission
def submitAssignment(student_id, assignment_name, link):
    """Submit an assignment"""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    query = f"INSERT INTO assignments (student_id, assignment_name, link) VALUES ('{student_id}', '{assignment_name}', '{link}')"
    cur.execute(query)

    conn.commit()
    conn.close()


# VULNERABILITY: SQL Injection in profile update
def updateProfile(student_id, email, phone):
    """Update student profile"""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    query = f"UPDATE users SET email = '{email}', phone = '{phone}' WHERE student_id = '{student_id}'"
    cur.execute(query)

    conn.commit()
    conn.close()


def getProfile(student_id):
    """Get student profile"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # This one is actually secure (using parameterized query)
    cur.execute("SELECT * FROM users WHERE student_id = ?", (student_id,))

    profile = cur.fetchone()
    conn.close()

    return profile


def getAnnouncements():
    """Get all announcements"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM announcements ORDER BY date DESC")

    announcements = cur.fetchall()
    conn.close()

    return announcements


# VULNERABILITY: SQL Injection in comments
def addComment(student_id, comment):
    """Add a comment"""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    query = f"INSERT INTO comments (student_id, comment, date) VALUES ('{student_id}', '{comment}', '{date}')"
    cur.execute(query)

    conn.commit()
    conn.close()


def getComments():
    """Get all comments"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT c.comment, c.date, u.name FROM comments c JOIN users u ON c.student_id = u.student_id ORDER BY c.date DESC")

    comments = cur.fetchall()
    conn.close()

    return comments


# Initialize database on import
init_db()
