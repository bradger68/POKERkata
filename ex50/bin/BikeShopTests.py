from assertions import printErrors, assertEqual
from BikeShop import *
from datetime import date, timedelta

yesterday = date.today() - timedelta(1)
today = date.today()
tomorrow = date.today() + timedelta(1)
steve = Customer(1, "Steve", "S.", yesterday)
jim = Customer(2, "Jim", "Jimsmith", tomorrow)
sam = Customer(3, "Sam", "Samsmith", yesterday)


assertEqual("Steve S.", steve.fullName())
assertEqual("Jim Jimsmith", jim.fullName())
assertEqual([steve,sam], customersToEmail([steve, jim,sam]))

printErrors()