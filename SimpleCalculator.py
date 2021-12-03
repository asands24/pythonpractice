#Simple Calculator

#Add two numbers together
def add(x, y):
	return x + y

#Subtract two numbers 
def subtract(x, y):
	return x - y 

#Multiply two numbers
def multiply(x, y):
	return x * y

#Divide two numbers
def divide(x, y):
	return x / y

print("Select Operation.")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

#While loop to ask for operation selection
while True:
	#prompt user for input 
	choice = input("Enter choice: (1, 2, 3, 4): ")
	#checks for the selection that was selected by user
	if choice in ('1', '2', '3', '4'):
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		if choice == '1':
			print(num1, "+", num2, "=", add(num1, num2))

		elif choice == '2':
			print(num1, "-", num2, "=", subtract(num1, num2))

		elif choice == '3':
			print(num1, "*", num2, "=", multiply(num1, num2))

		elif choice == '4':
			print(num1, "/", num2, "=", divide(num1, num2))
    # check if user wants another calculation
		next_calculation = input("Want to do another operation? (y/n)")
    # break the while loop if answer is no		
		if next_calculation == "n":
			print("Calulations completed.")
			break

	else:
		print("Invalid input")
