
class Exercises:

    # Exercise 1
    def circle_area(self):
        r = float(input("Enter circle radius? "))
        area = 3.14 * r * r
        print("Circle area =", area)

    # Exercise 2
    def temperature(self):
        c = float(input("Enter the temperature in Celsius? "))
        f = c * 9 / 5 + 32
        print(c, "(C) =", f, "(F)")

    # Exercise 3
    def prime_number(self):
        n = int(input("Enter a number? "))
        prime = True

        if n < 2:
            prime = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break

        if prime:
            print(n, "is a prime number")
        else:
            print(n, "is NOT a prime number")

    # Exercise 4
    def perfect_number(self):
        n = int(input("Enter a number? "))
        found = False

        for p in range(2, n):
            p_prime = True

            for i in range(2, p):
                if p % i == 0:
                    p_prime = False
                    break

            if p_prime:
                m = 2 ** p - 1
                m_prime = True

                for i in range(2, m):
                    if m % i == 0:
                        m_prime = False
                        break

                if m_prime and 2 ** (p - 1) * m == n:
                    found = True
                    break

        if found:
            print(n, "is a perfect number")
        else:
            print(n, "is NOT a perfect number")

    # Exercise 5
    def favorite_color(self):
        colors = ["Blue", "Yellow", "Red", "Black"]
        color = input("What is your favorite color? ")

        if color in colors:
            index = colors.index(color) + 1
            print("Your color is at index", index, "in my list")
        else:
            print("Sorry, I could not find your color")

    # Exercise 6
    def ranges(self):
        print(list(range(0, 7)))
        print(list(range(1, 11, 3)))
        print(list(range(5, 0, -1)))
        print(list(range(6, -3, -2)))

    # Exercise 7
    def remove_dollar(self):
        s = input("Enter a string: ")
        print(s.replace("$", ""))

    # Exercise 9
    def even_numbers(self):
        numbers = [0, 34, 23, 100, 999]
        result = []

        for x in numbers:
            if x % 2 == 0:
                result.append(x)

        print(result)

    # Exercise 10
    def factorial(self):
        n = int(input("Enter a number: "))

        if n < 0:
            print("Factorial is not defined for negative numbers")
            return

        result = 1

        for i in range(1, n + 1):
            result *= i

        print(result)

    # Exercise 11
    def divisors(self):
        n = int(input("Enter a number: "))

        if n == 0:
            print("Zero has infinitely many divisors")
            return

        result = []

        for i in range(1, abs(n) + 1):
            if n % i == 0:
                result.append(i)

        print(result)

    # Exercise 12
    def distance(self):
        x1, y1, x2, y2 = map(float, input(
            "Enter x1 y1 x2 y2: "
        ).split())

        result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        print(result)
