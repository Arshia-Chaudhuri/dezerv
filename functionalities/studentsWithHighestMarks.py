from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def students_with_highest_marks(courseId):
    try:
        pass
    except:
        return jsonify({'error': 'Something went wrong'}), 400