class Employee:
    name="Prince"
    language="Python"
    salary=100000
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "ITC InfoTech"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language.")        


a=Employee()
b=Programmer()

print(a.company,b.company)
b.show()
b.showlanguage()