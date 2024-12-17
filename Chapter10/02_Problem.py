# Write a class calculator capable of finding square, cube and squareroot of a number.

class calculator:
    def __init__(self, n):
        self.n = n

    def sqare(self):
        print(f"The sqaure is: {self.n * self.n}")

    def cube(self):
        print(f"The cube is: {self.n * self.n * self.n}")

    def sqaureroot(self):
        print(f"The sqaureroot is: {self.n ** 1/2}")

a = calculator(4)
a.greet()
a.sqare()
a.cube()
a.sqaureroot()
