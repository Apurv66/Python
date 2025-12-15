try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Division successful")

finally:
    # Always executes, whether an exception occurs or not.
    print("End of program")
