class Employee:
    name="Prince"
    company = "ITC"
    salary=10000000
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder(Employee):
    language="Python"
    def printlanguage(self):
        print(f"Out of all the language your language is: {self.language}")


class Programmer(Coder):
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language.")        


b=Programmer()

print(b.company)
print(b.language)
b.show()
b.printlanguage()
b.showlanguage()