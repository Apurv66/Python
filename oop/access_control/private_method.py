class A:
    def __method(self):  # Name-mangled method (not truly private)
        print("class A")

a = A()
# a.__method()  # Cannot be accessed directly from outside the class
a._A__method()  # Accessible via name mangling (discouraged)
