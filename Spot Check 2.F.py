import random

def getarray():
    array = []
    for count in range(1,6):
        array.append(count)
    return array

def number_generator(array):
    for count in range(20):
        number = random.randint(1,6)
        array.append(number)
    
    return array

def frequency(array):
    score = "Score"
    frequency = "Frequency"
    print("{0:5}  {1:11}".format(score, frequency))
    for counter in range(6):
        freq = 0
        for each in array:
            if each == counter + 1:
                freq = freq + 1
        print("{0:^5} {1:^11}".format(counter + 1, freq))

def main():
    array = getarray()
    array = number_generator(array)
    frequency(array)

main()


