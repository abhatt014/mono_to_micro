#flask app which displays all courses and which student enrolled in which course.
from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="mysql_db",
        user="appuser",
        password="redhat",
        database="schooldb"
    )
@app.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses ORDER BY id")
    courses = cursor.fetchall()
    db.close()

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT s.id, s.name, c.title AS course FROM students s JOIN courses c ON s.course_id = c.id;")
    students = cursor.fetchall()
    print(students)
    db.close()

    return render_template('index.html', courses=courses, students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)