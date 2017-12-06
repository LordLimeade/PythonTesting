class Person(object):
    """A person that works at an hourly or salary base job:

    Attributes:
        name: A string representing the customer's name.
        hourlyPay: the amount the person is paid for each hour of work.
        hoursWorked: the number of hours worked in a typical work week.
    """

    def __init__(self, name, hourlyPay, hoursWorked):
        """Return a Customer object whose name is *name*, hourly pay is *hourlyPay*, and whose hours worked each week is *hoursWorked*"""
        self.name = name
        self.hourlyPay = hourlyPay
        self.hoursWorked = hoursWorked
    
    def weekPay(self):
        """Return the amount of money the person would receive for one week of work."""
        pay = self.hourlyPay * self.hoursWorked
        return pay

    def calcSalary(self):
        """Return the estimated amount of money the person would receive in one 52-week year of work."""
        salary = (self.weekPay()) * 52
        return salary


