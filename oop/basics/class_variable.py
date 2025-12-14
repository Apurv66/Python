class A:
    count = 0 # class variable or static variable

    def __init__(self):
        A.count += 1

    @staticmethod
    def show():
        print(A.count)

obj = A()
A.show()