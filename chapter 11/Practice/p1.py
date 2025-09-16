class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")    

class TDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

a= TwoDVector(1,2)
b= TDVector(1,2,3)   
a.show()
b.show()     
                
        