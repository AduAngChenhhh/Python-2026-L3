
def add_students(system):
    system.add_students()


def add_courses(system):
    system.add_courses()


def add_marks(system):
    system.add_marks()


def run_exercises(exercises):
    while True:
        print("\n===== EXERCISES =====")
        print("1. Circle area")
        print("2. Temperature conversion")
        print("3. Prime number")
        print("4. Perfect number")
        print("5. Favorite color")
        print("6. Ranges")
        print("7. Remove dollar signs")
        print("8. Even numbers")
        print("9. Factorial")
        print("10. Divisors")
        print("11. Distance between two points")
        print("0. Back to main menu")

        choice = input("Choose an exercise: ")

        if choice == "1":
            exercises.circle_area()
        elif choice == "2":
            exercises.temperature()
        elif choice == "3":
            exercises.prime_number()
        elif choice == "4":
            exercises.perfect_number()
        elif choice == "5":
            exercises.favorite_color()
        elif choice == "6":
            exercises.ranges()
        elif choice == "7":
            exercises.remove_dollar()
        elif choice == "8":
            exercises.even_numbers()
        elif choice == "9":
            exercises.factorial()
        elif choice == "10":
            exercises.divisors()
        elif choice == "11":
            exercises.distance()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
