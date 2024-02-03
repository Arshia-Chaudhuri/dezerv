from flask import Flask, request, jsonify
from utils.db import db
from utils.seed import *
from functionalities.createStudents import *
from functionalities.fetchSingleStudent import *
from functionalities.fetchAllStudents import *
from functionalities.deleteSingleStudent import *
from functionalities.getCourseSingleStudent import *
from functionalities.createCourse import *
from functionalities.fetchSingleCourse import *
from functionalities.fetchAllCourses import *
from functionalities.deleteSingleCourse import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course_management.db'
db.init_app(app)

# 0. Seed the database with mock data
@app.route('/seed', methods=['GET'])
def index0():
    return seeding_database()

# 1. Create a student using POST mapping with API endpoint api/students/.
@app.route('/api/students', methods=['POST'])
def index1():
    return create_students()

# 2. Fetch a single student using GET mapping with API endpoint api/students/{id}.
@app.route('/api/students/<int:id>', methods=['GET'])
def index2(id):
    return fetch_single_student(id)

# 3. Fetch all students using GET mapping with API endpoint api/students/.
@app.route('/api/students/', methods=['GET'])
def index3():
    return fetch_all_students()

# 4. Delete a specific student using DELETE mapping with API endpoint api/students/{id}.
@app.route('/api/students/<int:id>', methods=['DELETE'])
def index4(id):
    return delete_single_student(id)

# 5. Get courses for a specific student using GET mapping with API endpoint api/students/{id}/courses.
@app.route('/api/students/<int:id>/courses', methods=['GET'])
def index5(id):
    return get_course_of_a_student(id)

# 6. Create a course using POST mapping with API endpoint api/courses/.
@app.route('/api/courses/', methods=['POST'])
def index6():
    return create_course()

# 7. Fetch a single course using GET mapping with API endpoint api/courses/{id}.
@app.route('/api/courses/<int:id>', methods=['GET'])
def index7(id):
    return fetch_single_course(id)

# 8. Fetch all courses using GET mapping with API endpoint api/courses/.
@app.route('/api/courses/', methods=['GET'])
def index8():
    return fetch_all_courses()

# 9. Delete a specific course using DELETE mapping with API endpoint api/courses/{id}.
@app.route('/api/courses/<int:id>', methods=['DELETE'])
def index9(id):
    return delete_single_course(id)

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(debug=True, port="8000") #####