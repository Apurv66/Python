# NOTE:
# Python does NOT support method overloading.
# This example shows WHY it fails.

class Shape:
    def area(self, r):
        return 3.14 * r * r

    def area(self, l, b):
        return l * b

s = Shape()
# print(s.area(4))  # Error: method overloading not supported
