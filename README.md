# Course management

Language used for backend development: Python (flask framework)

### API Codes used

- 200: OK
- 400: Bad request / Invalid argument (invalid request payload)
- 404: Not found
- 409: Conflict response status code indicates a request conflict with the current state of the target resource
- 415: Header is missing

### Project Hierarchy

```
project
    |- main.py
    |- enrollment_utilities
    |    |- enroll.py
    |    |- unenroll.py
    |    |- updateMmarks.py
    |- functionalities
    |    |- createStudent.py
    |    |- fetchSingleStudent.py
    |    |- fetchAllStudent.py
    |    |- deleteSingleStudent.py
    |    |- createCourse.py
    |    |- fetchSingleCourse.py
    |    |- fetchAllCourse.py
    |    |- deleteSingleCourse.py
    |    |- getCourseSingleStudent.py
    |    |- getStudentSingleCourse.py
    |- utils
    |    |- db.py
    |    |- seed.py
    |- instance
    |   |- course_management.db
    |- README.md
    |- images
        |- database_image.png
```

### Database Structure
![Database architecture](images/database_image.png)

### Running the Application
Install Flask:
```
pip install Flask
```
Install Flask SQLAlchemy:
```
pip install Flask-SQLAlchemy
```
Run the application:
```
python main.py
```
or
```
python main.py
```
The application will start running on `http://127.0.0.1:8000/`

### Seeding the Database with Mock Data
To seed the database with dummy data, I have added a separate route in the `main.py` file.

To seed the database with mock data just send a request to `/seed` with the `GET` method

### Testing on Postman