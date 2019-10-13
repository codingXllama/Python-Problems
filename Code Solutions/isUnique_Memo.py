

def isUnique(someStr):

    possibleChars = {}
    for item in someStr:
        if item not in possibleChars:
            possibleChars[item] = 1
            # print(possibleChars)
        else:
            return False
    return True



print(isUnique("abcde"))
print (isUnique('aaaaaa'))
print (isUnique('abcdefg'))
print (isUnique(''))
print (isUnique('abcdefghijklmnopqrstuvwxyzz'))
print (isUnique('abcdefghijklmnopqrstuvwxyz'))