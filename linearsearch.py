def search_list():
    searchlist =[]
    for count in range(10):
        item = input("Please enter a name to the list: ")
        searchlist.append(item)
    return searchlist

def search_item():
    searchitem = input("Please enter the item name you want to search for: ")
    return searchitem

def linear_search(searchlist, searchitem):
    found = False
    counter = 0
    while not found and counter < len(searchlist):
        if searchlist[counter] == searchitem:
            found = True
               
        counter = counter + 1
    return found
            

def display(searchitem, found):
    if found == True:
        print("{0} was found".format(searchitem))
    else:
        print("{0} was not found".format(searchitem))

def main():
    searchlist = search_list()
    searchitem = search_item()
    found = linear_search(searchlist, searchitem)
    display(searchitem, found)

main()
