print("Start Of The Program")

# Program to Count number of worsds from a file
count = 0
with open("New_text.txt", mode =  'r') as myFile:
    content = myFile.read()
    lines = content.split()
    count = len(lines)
    print(content)
print(count)

print("End Of The Program")