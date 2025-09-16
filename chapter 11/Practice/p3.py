class Employee:
    salary= 234
    increment =20

    @property
    def salaryincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryincrement.setter
    def salaryincrement(self,salary):
        self.increment=((salary/self.salary)-1)*100
    
e=Employee()
print(e.salaryincrement)
# e.salaryincrement =  300
print(e.increment)  