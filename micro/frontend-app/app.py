#fontend service app which displays index page
from flask import Flask, render_template,redirect,request
import requests
app = Flask(__name__)
COURSE_APP_URL = "http://course-app:5000"
STUDENT_APP_URL = "http://student-app:5000"
@app.route('/')
def index():
    # Fetch courses from course-app
    courses_response = requests.get(f"{COURSE_APP_URL}/courses")
    courses = courses_response.json() if courses_response.status_code == 200 else []
    # fetch students from student-app
    students_response = requests.get(f"{STUDENT_APP_URL}/students")
    students = students_response.json() if students_response.status_code == 200 else []
    return render_template('index.html',courses=courses,students=students)

@app.route('/courses', methods=['POST'])
def add_course():
    title = request.form.get('title')
    if title:
        # Send a POST request to course-app to add the course
        response = requests.post(f"{COURSE_APP_URL}/courses", json={"title": title})
        if response.status_code == 201:
            return redirect('/')
        else:
            return "Failed to add course", 400
    return "Invalid input", 400

@app.post('/students')
def add_student():
    name = request.form.get('name')
    course_id = request.form.get('course_id')
    if name and course_id:
        # Send a POST request to student-app to add the student
        response = requests.post(f"{STUDENT_APP_URL}/students", json={"name": name, "course_id": course_id})
        if response.status_code == 201:
            return redirect('/')
        else:
            return "Failed to add student", 400
    return "Invalid input", 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)