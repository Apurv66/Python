with open("sample.txt", "r") as f:
    print(f.read(5))
    f.seek(0)       # Moves the file cursor back to the beginning of the file
    print(f.read())
