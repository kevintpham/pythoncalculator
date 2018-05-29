

# This function multiplies 2 numbers

def multiplicationFunction(num1,num2):
	Result = num1 * num2
	return Result

#This function adds 2 numbers
def additionFunction(num1,num2):
	Result = num1 + num2
	return Result

#This function subtracts 2 numbers
def subtractionFunction(num1,num2):
	Result = num1 - num2
	return Result

#This function divides 2 numbers
def divisionFunction(num1,num2):
	Result = num1 / num2
	return Result

#This function takes the first number to the power of the second number
def exponentFunction(num1,num2):
	Result = num1 ** num2
	return Result


#Prints out math options

print("Select your weapon.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")

 
#Asks the user to enter their desired mathematical operator and two numbers

choice = input("Enter choice(1/2/3/4/5):")



num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

#Variables needed to be able to print out the output

Multiplication = multiplicationFunction(num1,num2)
Addition = additionFunction(num1,num2)
Subtraction = subtractionFunction(num1,num2)
Division = divisionFunction(num1,num2)
Exponent = exponentFunction(num1,num2)

#Depending on choice of mathematical operator, joins both of the users numbers togethers

if choice == '1':
	print(Addition)
elif choice == '2':
	print(Subtraction)
elif choice == '3':
	print(Multiplication)
elif choice == '4':
	print(Division)
elif choice == '5':
	print(Exponent)
else:
	print("You shall not pass your math test!!!")

