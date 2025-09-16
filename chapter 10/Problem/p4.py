class calculator:

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The squarre is : {self.n*self.n}")

    def cube(self):
        print(f"The squarre is : {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square root  is : {self.n**(1/2)}")

    @staticmethod
    def hello():
        print("Hello There!!")    
n=int(input("Enter any NO:"))
a= calculator(n)
a.square()      
a.cube()
a.squareroot()      
