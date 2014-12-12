##Result ←  0
##Index ←  0
##Repeat
##    Index ←  Index + 1
##    If Result < Values[Index]
##        Then Result ←  Values[Index]
##    EndIf
##Until Index = 4
##

Values = [24,13,57,45]
Result = 0
Index = 0

while Index < 4:
    
    if Result < Values[Index]:
        Result = Values[Index]
    Index = Index + 1

print(Result)
        
