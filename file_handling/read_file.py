f = open("sample.txt", "r")
print(f.read()) # Reads the full file content; you can pass a number to read limited characters (like f.read(5))

f.close()