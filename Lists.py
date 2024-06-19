print("Start Of The Program")

# Smallest And Largest Number in List
print("Program to find Smallest And Largest Number in List")
list1= []
while True:
    x = int(input("Enter number: "))
    list1.append(x)
    res = input("Continue [Y/N]: ")
    if res == 'N':
        break

list1.sort()
list_size = len(list1)
print("Smallest Value of list: ", list1[0])
print("Largest Value of list: ", list1[list_size-1])
print(list1)

# Removing Duplicates from list
print("Program to remove duplicates from list")
list2 = []
while True:
    x = int(input("Enter number: "))
    list2.append(x)
    res = input("Continue [Y/N]: ")
    if res == 'N':
        break

list2 = list(set(list2))
print(list2)
print("End Of The Program")