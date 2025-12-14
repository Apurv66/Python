class A:
    def __init__(self):
        self.__password = 1234  # Name-mangled attribute (not truly private)
    
    def show(self):
        print(self.__password)

a = A()

# a.__password  # Not accessible directly (AttributeError)

a.show()        # Works inside the class

# Python doesn't have true private variables.
print(a._A__password)  # Still accessible using a._A__password
