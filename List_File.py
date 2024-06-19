print("Start Of The Program")

# program to store a integer list in file
count = 0
list1= []
while True:
    x = int(input("Enter number: "))
    list1.append(x)
    res = input("Continue [Y/N]: ")
    if res == 'N':
        break
with open("Integer_List.txt", mode =  'w') as myFile:
        myFile.write(str(list1))
with open("Integer_List.txt", mode='r') as myFile:
    content = myFile.read()
    print(content)

print("End Of The Program")