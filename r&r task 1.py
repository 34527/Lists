counter = 1
studentlist = []

for count in range(8):
    studentlist.append(input("Please enter a students name: "))


for each in studentlist:
    print("{0}. {1}".format(counter, each))
    counter = counter + 1

count = 1
    
change = int(input("Please enter the student you wish to change: "))

true_change = change - 1

studentlist.pop(true_change)
studentlist.insert(true_change, input("please enter the new name: "))

for each in studentlist:
    print("{0}. {1}".format(count, each))
    count = count + 1
