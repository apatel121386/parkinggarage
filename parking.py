 master
class ParkingGarage():

    
    def __init__(self, tickets, currentTicket):
        self.tickets = tickets
        self.currentTicket = currentTicket
    def takeTicket(self, ticketNum):
        self.currentTicket[ticketNum] = ''
        self.tickets.remove(ticketNum)
    def payForParking(self, payTicket):
        self.payTicket = payTicket
        value = int(input("enter space number "))
        if value is not None:
            self.currentTicket[payTicket] = "paid"
            print("ticket has been paid and you may leave")
            tickets.append(int(value))

    def leaveGarage(self, ticketNum):
        if self.currentTicket[int(ticketNum)] == 'paid':
            self.tickets.append(int(ticketNum))
            self.tickets.sort()
            print("Thank you, have a nice day")
        else:
            print("Thank you")

tickets = [1, 2, 3, 4, 5]
currentTicket = {}


garage = ParkingGarage(tickets, currentTicket)

def runGarage():
    while True:
        value = input("Would you like to park/pay or leave?: ")
        if value.lower() == "park":
            if tickets != []:
                ticketNum = tickets[0]
                garage.takeTicket(ticketNum)
                print("Parking available:")
                print(tickets)
            else:
                print("No parking available")
        elif value.lower() == "pay":
            money = 0
            pay = int(input("How many hours did you park? "))
            if pay <(1):
                print("free parking")
            elif pay <(2): 
                print("payment due: $10")
                money = money +10
            elif pay < (3): 
                print("payment due: $20")
                money = (money + 20)
            elif pay < (4): 
                print("payment due: $30")
                money = (money + 30)
            elif pay < (5): 
                print("payment due: $40")
                money = (money + 40)
            elif pay >= (5): 
                print("payment due: $50")
                money = (money + 50)
            garage.payForParking(pay)
        elif value.lower() == "leave":
            ticketNum = input("What is your ticket number?: ")
            garage.leaveGarage(ticketNum)
            print("Parking available:")
            tickets.sort()
            print(tickets)
        else:
            print("Command not recognized")


runGarage() 

class ParkingGarage():
    
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self, ticketNum):
        self.currentTicket[ticketNum] = ''
        self.tickets.remove(ticketNum)
        self.parkingSpaces.remove(ticketNum)

    def payForParking(self, payTicket):
        self.payTicket = payTicket
        value = input("Please press any key to pay: ")
        if value is not None:
            self.currentTicket[payTicket] = "paid"
            print("ticket has been paid and you may leave")

    def leaveGarage(self, ticketNum):
        if self.currentTicket[int(ticketNum)] == 'paid':
            print("Thank you, have a nice day")
            self.tickets.append(int(ticketNum)) 
            self.parkingSpaces.append(int(ticketNum))
            self.tickets.sort()
            self.parkingSpaces.sort()
        else:
            print("Must pay first")

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
currentTicket = {}

garage = ParkingGarage(tickets, parkingSpaces, currentTicket)

def runGarage():
    while True:
        value = input("Would you like to park/pay or leave?: ")
        if value.lower() == "park":
            if tickets != []:
                ticketNum = tickets[0]
                garage.takeTicket(ticketNum)
                print("Parking available:")
                print(tickets)
            else:
                print("No parking available")
        elif value.lower() == "pay":
            pay = input("What parking space would you like to pay for?: ")
            garage.payForParking(pay)
        elif value.lower() == "leave":
            ticketNum = input("What is your ticket number?: ")
            garage.leaveGarage(ticketNum)
            print("Parking available:")
            print(tickets)
        else:
            print("Command not recognized")

runGarage()
 master
