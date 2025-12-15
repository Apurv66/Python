try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Please enter valid integers")

except Exception as e:
    print(e)