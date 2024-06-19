print("Start Of The Program")
list1= []
while True:
    x = int(input("Enter number in list1: "))
    list1.append(x)
    res = input("Continue [Y/N]: ")
    if res == 'N':
        break

list2 = []
while True:
            x = int(input("Enter number in list 2: "))
            list2.append(x)
            res = input("Continue [Y/N]: ")
            if res == 'N':
                break

set_list1=set(list1)
set_list2=set(list2)
common_list = set_list1.intersection(set_list2)
print(common_list)
print("End Of The Program")