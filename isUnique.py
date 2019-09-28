'''

Chapter 01 - Problem 01 - Is Unique - CTCI 6th Edition page 90

Problem Statement:
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Example:

"aalex" -> False

'''


def isUnique(s1):
    return len(s1)==len(set(s1.lower()))



print(isUnique("RueE"))
print(isUnique("aalex"))


print (isUnique('aaaaaa'))
print (isUnique('abcdefg'))
print (isUnique(''))
print (isUnique('abcdefghijklmnopqrstuvwxyzz'))
print (isUnique('abcdefghijklmnopqrstuvwxyz'))