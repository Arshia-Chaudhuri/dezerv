from flask import Flask, request, jsonify
import json
from utils.db import db, Student, Course, Enrollment
from functionalities.fetchSingleStudent import *

def get_student_of_a_course(id):
    try:
        course = Course.query.get(id)

        if course is None:
            return jsonify({'error': 'Course is not found'}), 404

        enrollment = Enrollment.query.filter_by(courseId = id).all()

        if enrollment is None:
            return jsonify({'message': 'The course is not registered by any student'})

        result = []
        for each in enrollment:
            curr_studentId = each.studentId
            student_data = fetch_single_student(curr_studentId, internally=True)
            result.append(student_data)
        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400