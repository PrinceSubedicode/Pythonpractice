class Comolex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

def __add__(self,c2):
    return complex(self.r+c2.r,self.i+c2.i)

c1=complex(2,4)
c2=complex(3,5)
c3=c1+c2
print(c3)

        