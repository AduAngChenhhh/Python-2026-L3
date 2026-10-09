
from domains.student import Student
from domains.course import Course


class StudentManagement:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def add_students(self):
        n = int(input("Number of students: "))

        for i in range(n):
            id = input("ID: ")
            name = input("Name: ")
            dob = input("DoB: ")

            self.students[id] = Student(id, name, dob)

        print("Students added successfully!")

    def add_courses(self):
        n = int(input("Number of courses: "))

        for i in range(n):
            id = input("Course ID: ")
            name = input("Course name: ")

            self.courses[id] = Course(id, name)

        print("Courses added successfully!")

    def add_marks(self):
        if not self.students:
            print("Please add students first!")
            return

        course = input("Course ID: ")

        if course not in self.courses:
            print("This course doesn't exist. Please choose again!")
            return

        if course not in self.marks:
            self.marks[course] = {}

        for id in self.students:
            mark = input(
                "Mark for " + self.students[id].name + ": "
            )
            self.marks[course][id] = mark

        print("Marks added successfully!")
