class A:
    def __init__(self):
        print("class A constructor")

class B(A):
    def __init__(self):
        print("class B constructor")

b = B()
