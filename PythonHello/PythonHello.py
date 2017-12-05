from decimal import Decimal

print ("Hello Python!")
four = 2 + 2
print ("2 + 2 =", four)
check = True

while (check):
    try:
        hourly = Decimal(input("How much do you make per hour?\n" ))
        hours = int(input("How many hours do you work each week?\n" ))
        weekly = hourly * hours
        salary = weekly * 52
        print("Your Salary is ${0} dollars.".format(salary))
        check = False
    except:
        print ("Please enter a valid number")

print ("Have a nice day")



