#course-app service app which manages courses
from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="mysql_db",
        user="appuser",
        password="redhat",
        database="schooldb"
    )
@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        if title:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO courses (title) VALUES (%s)", (title,))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Course added"}), 201
        return jsonify({"error": "Invalid input"}), 400
    else:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(courses)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)        