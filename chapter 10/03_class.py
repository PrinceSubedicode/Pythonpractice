class Employee:
    salary=2000000
    language="py"

    def get_info(self):
        print(f"The language is:{self.language}. The salary is {self.salary}.")
    
    @staticmethod
    def greet():
        print("Good Morning...")
a=Employee()
a.get_info()
a.greet()
# Employee.get_info(a)