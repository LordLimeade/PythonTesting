from decimal import Decimal
from Classes.Person import Person
import sys
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calculate():
    cls()

    person = None
    saveProfile = False
    yesNo = "n"

    person = getValues()
    output(person)
    
    yesNo = str(input("Would you like to save this profile? (Y/N)\n"))

    while (yesNo.lower() != "y") and (yesNo.lower() != "n"):
        yesNo = input("Please enter Y or N to continue.\n")

    if (yesNo.lower() == "y"):
        #do the saving thing
        print("Profile Saved.")
        input("Press enter to return to the main menu.")
    elif (yesNo.lower() == "n"):
        print("Profile Not Saved.")
        input("Press enter to return to the main menu.")
    

def display():
    cls()
    print("This displays things")
    input("Press enter to return to the menu...\n")

def exit():
    cls()
    sys.exit(0)

def default():
    cls()
    print("Something went wrong...")

getOptions = {
            0 : default,
            1 : calculate,
            2 : display,
            3 : exit,
}

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


def menu():
    while (True):
        cls()

        print("Please select an option to continue.")
        print("1: Calculate weekly pay and salary.")
        print("2: Display saved profiles.")
        print("3: Exit application.")

        option = 0

        try:
            option = int(input(""))
        except:
            cls()
            input("value must be a number. Press enter to try again...")
            continue

        getOptions[option]()

menu()






