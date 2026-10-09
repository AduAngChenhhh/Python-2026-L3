
def show_students(system):
    if not system.students:
        print("No students available!")
        return

    for id in system.students:
        student = system.students[id]
        print(student.id, student.name, student.dob)


def show_courses(system):
    if not system.courses:
        print("No courses available!")
        return

    for id in system.courses:
        course = system.courses[id]
        print(course.id, course.name)


def show_marks(system):
    while True:
        course = input("Course ID (or 0 to go back): ")

        if course == "0":
            return

        if course not in system.courses:
            print("This course doesn't exist. Please choose again!")
            continue

        if course not in system.marks or not system.marks[course]:
            print(
                "This course hasn't been marked yet. "
                "Please choose again!"
            )
            continue

        print("Course:", system.courses[course].name)

        for id in system.marks[course]:
            print(
                system.students[id].name,
                ":",
                system.marks[course][id]
            )

        break
