import random
countries = ["England", "Germany", "Spain", "France"]
capitals = ["London", "Berlin", "Madrid", "Paris"]
numbercorrect = 0


for count in range(5):
    selection = random.randint(0,3)
    answer = input("What is the capital of {0}? ".format(countries[selection]))
    if answer == capitals[selection]:
        numbercorrect = numbercorrect + 1


print("You got {0} correct".format(numbercorrect))

    
    




                                                   
