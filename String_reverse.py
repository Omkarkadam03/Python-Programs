print("Start Of The Program")

# Program To Reverse the Given String
str1 = input("Enter some String: ")
rev_str = ""

for x in str1.split():
    rev_str = x +" " +rev_str
print("Reversed String is: ", rev_str)

print("End Of The Program")