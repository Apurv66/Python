class A:
    def __init__(self):
        print("class A constructor")

    def show(self):
        print("class A method")

class B(A):
    def __init__(self):
        print("class B constructor")
        super().__init__()  # Call parent class constructor

    def show(self):
        print("class B method")
        super().show()      # Call parent class method

b = B()
b.show()
