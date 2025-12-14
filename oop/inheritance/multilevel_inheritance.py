class A:
    def show1(self):
        print("class A")

class B(A):
    def show2(self):
        print("class B")

class C(B):
    def show3(self):
        print("class C")

c = C()
c.show1()
c.show2()
c.show3()