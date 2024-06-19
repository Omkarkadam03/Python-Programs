print("Start Of The Program")

# Check wether the number is evwn or odd
num1= int(input("Enter number: "))
if num1 % 2 == 0:
    print("No is even")
else:
    print("Number is odd")

# Printing prime number from 1 to 100
print("Prime Number from 1 to 100")
n = 2
while n<= 100:
    i = 2
    flag = 0
    while i < n:
        if n % i == 0:
            flag =  1
            break
        i = i + 1
    if flag == 0:
                print(n)
    n = n + 1

print("End Of The Program")
