# Can you change the self parameter inside a class to something else. Try changing self to 'sf' and see the changes.

from random import randint

class Train:
    def __init__(sf, trainNo):
        sf.trainNo = trainNo

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