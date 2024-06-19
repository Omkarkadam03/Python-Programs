print("Start Of The Program")

str1 = input("Enter some string: ")
words = str1.split()
words_count = {}
for item in words:
    if item in words_count:
        words_count[item] +=1
    else:
        words_count[item] = 1
print(words_count)
print("End Of The Program")