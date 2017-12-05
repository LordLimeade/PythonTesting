from decimal import Decimal

def getValues():
        check = True

        while (check):
            try:
                pay = Decimal(input("How much do you make per hour?\n" ))
                worked = int(input("How many hours do you work each week?\n" ))
                
                check = False
            except:
                print ("Please enter a valid number")

        return pay, worked

def calcs(hourly, hours):
    weekly = hourly * hours
    salary = weekly * 52
    return salary

def output(salary):
    print("Your Salary is ${0} dollars.".format(salary))

print ("Hello Python!")
four = 2 + 2
print ("2 + 2 =", four)


hourly = 0.0
hours = 0
salary = 0

hourly, hours = getValues()

salary = calcs(hourly, hours)

output(salary)

print ("Have a nice day")






