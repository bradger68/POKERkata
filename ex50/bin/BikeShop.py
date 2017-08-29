from datetime import date, timedelta

class Customer:
    def __init__(self, identity, firstName, lastName, fixDate):
        self.firstName = firstName
        self.lastName = lastName 
        self.identity = identity
        self.fixDate = fixDate
        
     
    def fullName(self):
        return self.firstName + " " + self.lastName
        
def customersToEmail(Customers):
    validCustomers = []
    for customer in Customers:
        if customer.fixDate <= date.today():
            validCustomers.append(customer)
    return validCustomers