data = ["hello", " world\n", "how are you?"]

f = open("sample.txt", "w")
f.writelines(data)

f.close()