try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Your age is:", age)

except Exception as e:
    print(e)
