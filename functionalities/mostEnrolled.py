from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment
from functionalities.getStudentSingleCourse import *
from functionalities.fetchSingleCourse import *

def most_enrolled():
    try:
        course_ids = Course.query.with_entities(Course.courseId).all()
        course_ids = [course_id for (course_id,) in course_ids]
        number_of_students = 0
        course_names = []

        # fetching naximum number of students
        for course_id in course_ids:
            all_students_of_this_course = get_student_of_a_course(course_id, internally=True)
            total_number = len(all_students_of_this_course)
            if total_number > number_of_students:
                number_of_students = total_number

        for course_id in course_ids:
            all_students_of_this_course = get_student_of_a_course(course_id, internally=True)
            total_number = len(all_students_of_this_course)
            if total_number == number_of_students:
                course_names.append(fetch_single_course(course_id, internally=True)['courseName'])
        result = {
            'maximum_students_enrolled': number_of_students,
            'courses': course_names
        }
        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400