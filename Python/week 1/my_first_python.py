# Python Basics
import math as m
import module_example as myCode

print("Hello World!!")  # saying hello world

""" 
Comment 
Tgnina
"""

if 10 < 20:
    print("10 is less than 20")

# name = input("whats ur name = ")
name = "Jericho"
age = 19

print(type(name))

# below breaks bcuz not concat wit strings
#print (name+ " is ur name and " + age + "is ur age")
#print(f"{name} is ur name and {age} is ur age")

print(name + " is ur name and " + str(age) + " is ur age")
print(f"{name} is ur name and {age} is ur age")

print(m.ceil(3.2))
print(m.floor(3.2))

myCode.welcome("ireee")

new_string = myCode.variableString
print(new_string)

# print ( dir(m) )

try:
    print(1+1)
except:
    print(2+2)
