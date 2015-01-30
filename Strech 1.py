placename_list = ["Newcastle", "Carlisle", "Workington", "Cambridge", "London"]

print("Current List")
for each in enumerate(placename_list):
    print(each)

def menu():
    print("1. Add an item to the end of the list")
    print("2. Delete an item by name")
    print("3. Delete an item by list position")
    print("4. Insert a new item")
    print("5. Amend an item")
    print("9. Exit")
    
def selection():
    selection = input("Please enter a selection: ")
    return selection


def selection_choice(selection):
    if selection == 1:
        placename_list.append(input("Please enter an item to add to the end of the list: "))
    elif selection == 2:
        remove = input("Please enter the name what you want to remove from the list")
        return remove   #what the user wants to remove from the list (by name)
    elif selection == 3:
        position_remove = int(input("Please enter the postion of the item you want to remove: "))
        return position_remove      #what the user wants to remove from the list (by position)
    elif selection == 4:
        insert_location = int(input("Please enter where you want the item to be inserted into the list: "))
        insert_item = input("Please enter what you want to insert into the list: "))
        return insert_location, insert_item
    elif selection == 5:
        amend_location = int(input("Please enter the location of the item you want to amend: "))
        amend_item = input("Please enter the amended item: "))
        return amend location
    elif selection == 9:
    else:
        print("Invalid")
        
        
                              


def main():
    menu()
    selection = selection()
    selection_choice()
