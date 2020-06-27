def isPalindrome(foo):
    return foo == foo[::-1]


userInput = input("Enter a string: ")

soln = f"{userInput} is a Palindrome" if isPalindrome(
    userInput.lower()) == True else f"{userInput} is not a palindrome"


print(soln)
