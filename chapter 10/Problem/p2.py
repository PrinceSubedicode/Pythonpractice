class calculator:

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The squarre is : {self.n*self.n}")

    def cube(self):
        print(f"The squarre is : {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squarre is : {self.n**(1/2)}")

a= calculator(16)
a.square()      
a.cube()
a.squareroot()      