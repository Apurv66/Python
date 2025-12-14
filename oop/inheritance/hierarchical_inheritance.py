class A:
    def show1(self):
        print("class A")

class B(A):
    def show2(self):
        print("class B")

class C(A):
    def show3(self):
        print("class C")

b = B()
c = C()

b.show1()
b.show2()
c.show1()
c.show3()
