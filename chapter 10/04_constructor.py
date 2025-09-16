class Employee:
    salary=2000000
    language="py"

    def __init__(self,name,salary,language):  #dunder method which is automatically called 
        self.name= name
        self.salary= salary
        self.language= language
        print("I am creating an objects..")


    def get_info(self):
        print(f"The language is:{self.language}. The salary is {self.salary}.")
    
    @staticmethod
    def greet():
        print("Good Morning...")
a=Employee("Prince",1200000,"JavaScript")  # directly pass the objects using the constructor
a.get_info()
a.greet()