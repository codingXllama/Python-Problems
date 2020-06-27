def isPrime(num):

    if num >= 2:

        for val in range(2, num):
            if num % val == 0:
                return False
            else:
                return True

    return False


userInput = int(input("Enter a number to check if it's prime or not: "))
soln = "prime" if int(isPrime(userInput)) == 1 else "not prime"
print(soln)
