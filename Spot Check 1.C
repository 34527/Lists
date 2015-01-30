scores = [18, 23, 36, 21, 58, 40, 45, 59]
max = 8
count1 = 1
count2 = 1

for count1 in range(max - 1):
    for count2 in range(max-1):
        if scores[count2] > scores[count2 + 1]:
            temp = scores[count2]
            scores[count2] = scores[count2 + 1]
            scores[count2 + 1] = temp


print(scores)
        
    
