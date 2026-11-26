#flask app which displays all courses and which student enrolled in which course.
from flask import Flask, render_template,request,redirect
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

@app.post('/courses')
def add_course():
    title = request.form['title']
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("INSERT INTO courses (title) VALUES (%s)", (title,))
    db.commit()
    db.close()
    return redirect('/')
@app.post('/students')
def add_student():
    name = request.form['name']
    course_id = request.form['course_id']
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("INSERT INTO students (name, course_id) VALUES (%s, %s)", (name, course_id))
    db.commit()
    db.close()
    return redirect('/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)