# Hybrid inheritance is combination of two or more types of inheritance
class A:
    def show1(self):
        print("class A")

class B:
    def show2(self):
        print("class B")

class C(A):
    def show3(self):
        print("class C")

class D(B, C):
    def show4(self):
        print("class D")

d = D()
d.show1()
d.show2()
d.show3()
d.show4()
