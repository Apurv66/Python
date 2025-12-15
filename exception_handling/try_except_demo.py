try:    
    # Used when we are not sure whether the code will produce an error or not.
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)

except Exception as e:  
    # Executes only when an exception occurs in the try block. It is used to handle errors.
    print(e)
    print(e.with_traceback)

