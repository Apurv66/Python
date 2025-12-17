with open('sample.txt', 'r') as f:
    print(f.read(5))
    print(f.tell()) # Returns the current position of the file cursor