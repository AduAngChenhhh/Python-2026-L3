
from domains.student_management import StudentManagement
from domains.exercises import Exercises

from input import add_students, add_courses, add_marks, run_exercises
from output import show_students, show_courses, show_marks


def main():
    system = StudentManagement()
    exercises = Exercises()

    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add students")
        print("2. Add courses")
        print("3. Add marks")
        print("4. Show students")
        print("5. Show courses")
        print("6. Show marks")
        print("7. Exercises")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_students(system)

        elif choice == "2":
            add_courses(system)

        elif choice == "3":
            add_marks(system)

        elif choice == "4":
            show_students(system)

        elif choice == "5":
            show_courses(system)

        elif choice == "6":
            show_marks(system)

        elif choice == "7":
            run_exercises(exercises)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
