try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    # Executes only when no exception occurs in the try block.
    # It does not execute if an error occurs.
    print("Division successful")