print("Start Of The Program")
# Function To find The factorial
def fact(num):
    while num>0:
        return num*fact(num-1)
    else:
        return  1
Number = int(input("Enter  no:"))
result =fact(Number)
print("factorial of {0} is {1}".format(Number, result))

# Function To find The factorial
def palidrome_check():
    str1 = input("Enter some String: ")
    rev_str = ""
    for x in str1:
        rev_str = x + rev_str
    if rev_str == str1:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

palidrome_check()
print("End Of The Program")