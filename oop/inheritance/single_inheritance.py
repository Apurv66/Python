class A:
    def show1(self):
        print("class A")

# B class inheriting from A
class B(A):
    def show2(self):
        print("class B")

b = B()
b.show1()
b.show2()
