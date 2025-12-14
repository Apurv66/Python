class A:
    def __init__(self, name):
        self.name = name   # instance variable
    
    def show(self):
        print("Name:", self.name)

a = A("Rohan")
b = A("Vijay")
a.show()
b.show()
