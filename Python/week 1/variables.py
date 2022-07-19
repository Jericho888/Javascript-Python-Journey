# Python Variables
import math

"""
	1.) Create three string variables called myName, parentName1 
	and parentName2 and assign them values. Then in a single sentence 
	print out "My name is X. My parents' names are Y and Z"
"""
print("\nQ 1.")
myName = "Jericho"
pName = "Mary "
pName2 = "Benson "
print("My name is " + myName + "." +
      " My parents name are " + pName + "and " + pName2)

"""
	2.) Create a string variable called petName and give it a string value. 
	Create an integer and call it petAge and assign it a value. Print the
	sentence "X is my pet and they are Y years old". Make sure to cast the
	petAge variable as a string before outputting the sentence.
"""
print("\nQ 2.")
petName = "Goldie "
petAge = "9"

print(petName + " is my pet" + " and " + " they are " + petAge + " yearsold.")


"""
	3.) Four strings are provided below representing files. They have file 
	extensions such as .txt, .html and .js at the end. Print out each file name 
	without the file extension. Only remove the file extension from the end
"""
print("\nQ 3.")
s1 = "homework.txt"
s2 = "assignment2.html"
s3 = "main.js"
s4 = "js.mainjs.js"

s1_new = s1.strip(".txt")


print(s1.strip(".txt"))
print(s2.strip(".html"))
print(s3.strip(".js"))
print(s4.strip(".js"))


"""
	4.) Four strings are provided below. Update each one of the strings by
	removing all numbers that appear inside them and uppercase the first
	letter. Then in a single sentence print out each new string separated
	by commas e.g. Apple, Orange, Lemon, Tea
"""


print("\nQ 4.")


f1 = "ap12ple"
f2 = "oran454ge"
f3 = "9lem5on5"
f4 = "t12ea"

f1_new = f1.replace("12", "")

print(f1_new + "," + (f2.replace("454", "")) + "," +
      (f3.replace("9", "", )) + "," + (f4.replace("12", "")))


"""
	5.) Ask the user to type in their name using input(). Then replace
	all occurences of the letter "a" with "x", and print the following
	"Welcome Nxme! Your name is Y letters long." where Nxme is their 
	inputted converted name and Y is the number of characters in the name. 
	Note that the first letter is capitalized, all subsequent letters are 
	lowercase and all "a"s are replaced with "x".
"""
print("\nQ 5.")


"""
	6.) Create an integer called age and another called year and assign them 
	the values of your age and the current year. Then print a single
	sentence that says "My age is X and I was born in the year YYYY" where
	YYYY is year - age.
"""
print("\nQ 6.")


"""
	7.) Do the exact same as above except this time ask the user to input their
	age and the current year
"""
print("\nQ 7.")


"""
	8.) There are two variables below representing a temperature in Celsius
	and one in Fahrenheit. Write code that converts the temperatures to the
	opposite scale and print 2 sentences reading "X degrees Celsius is Y degrees 
	Fahrenheit" and vice versa for the other one.
"""
print("\nQ 8.")
tempFahrenheit = 32
tempCelsius = 25


"""
	9.) Calculate the area of a circle that has a radius of 45.5cm. Use
	the correct and accurate value of a pi. Display this result like 
	"6503.882cm^2". Note the area is rounded to three decimal places
"""
print("\nQ 9.")
