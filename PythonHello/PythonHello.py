from decimal import Decimal
from Classes.Person import Person
import sys
import time

def getValues():
        check = True

        name = ""
        pay = 0.0
        worked = 0
        counter = 0

        while (check):
            try:
                name = str(input("What is your name?\n"))
                pay = Decimal(input("How much do you make per hour?\n" ))
                worked = int(input("How many hours do you work each week?\n" ))
                
                check = False
            except:
                print ("One of your values was invalid please try again.")

        person = Person(name, pay, worked)

        check = True
        while(check):
            try:
                person = Person(name, pay, worked)
                check = False
                return person
            except:
                print ("Something went wrong making your profile.")
                counter += 1
                if (counter > 9):
                    print("\n\nProblem could not be resolved. Closing application")
                    time.sleep(3)
                    sys.exit(0)
        

def output(person):
    print("Your weekly pay is ${0} dollars.".format(person.weekPay()))
    print("Your Salary is ${0} dollars.".format(person.calcSalary()))

person = None

person = getValues()

output(person)

print ("Have a nice day")






