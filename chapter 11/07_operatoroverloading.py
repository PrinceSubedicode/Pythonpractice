class Animal:
    def __init__(self,name):
        self.name=name

    def __add__(self,other):
            #overloading add operator to combine the name of two animal 
        return Animal(self.name + "&" + other.name)    
    
    def speak(self):
        return f"{self.name} Speaks!!"
    

a1=Animal("Dog")
a2=Animal("cat")    
a3=a1+a2
print(a3.speak())