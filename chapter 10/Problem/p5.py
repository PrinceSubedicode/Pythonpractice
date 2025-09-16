import random
# from random import randint    if we use this we dirctly use randint below 
class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def book(self,fro,to):
        print(f"Ticket is Booked in trainNO: {self.trainNo} from {fro} to {to}")


    def getstatus(self):
        print(f"Train is Sucessfully running , train no: {self.trainNo}")


    def getFare(self, fro, to):
        print(f"Ticket is Fare in trainNO: {self.trainNo} from {fro} to {to} is {random.randint(111,555)}")


t=Train(12345)
t.book("Kathmandu","Pokhara")
t.getstatus()
t.getFare("Kathmandu","Pokhara")
