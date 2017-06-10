# Test Helper
from __future__ import print_function
errorlist = []
def assertEqual(a, b):
    if(a != b):
        print('F', end='')
        errorlist.append("Test Failed. Expected: " + str(a) + " but found: " + str(b))
    else:
        print('.', end='')
        
def printErrors():
	print(" ")
	print(" ")
	for error in errorlist:
		print(error)