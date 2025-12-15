# Creating a custom exception
class NegativeNumberError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise NegativeNumberError("Age cannot be negative")

    print("Your age is:", age)

except NegativeNumberError as e:
    print("Custom Exception:", e)

except Exception as e:
    print(e)
