print("Start Of The Program")

str1 = input("Enter some String: ")
vowel_Count = 0
for x in str1:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x =='u':
        vowel_Count += 1
print("Total number of vowels: ", vowel_Count)

print("End Of The Program")