print("Start Of The Program")

#Input By User
num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

#Basic Arithmatic Operations
print("Addition: ",(num1 + num2))
print("Subtraction: ",(num1 - num2))
print("Multiplication: ",(num1 * num2))
print("Division: ", (num1 / num2))

#Swaping Two number Without Third Variable
print("Before Swap: num1 is {0} and num2 is {1}".format(num1, num2))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After Swap: num1 is {0} and num2 is {1}".format(num1, num2))

print("End Of The Program")