#student-app service app which manages students
from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)
# Database configuration
def get_db_connection():
    return mysql.connector.connect(
        host='mysql_db',
        user='appuser',
        password='redhat',
        database='schooldb'
    )
@app.route('/students', methods=['GET', 'POST']) 
def students():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        course_id = data.get('course_id')
        if name and course_id:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (name, course_id) VALUES (%s, %s)", (name, course_id))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Student added"}), 201
        return jsonify({"error": "Invalid input"}), 400
    else:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT s.id, s.name, c.title AS course FROM students s JOIN courses c ON s.course_id = c.id;")
        students = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(students)   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)        