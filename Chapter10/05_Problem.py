# Write a class train which has methods to book a ticket, get status (no. of seats) and get fare information of trains running unser Indian Railways.
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def gatFare(self, fro, to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(1000,5000)}")


t = Train(12399)
t.book("Chandigarh", "Delhi")
t.getStatus()
t.gatFare("Chandigarh", "Delhi")