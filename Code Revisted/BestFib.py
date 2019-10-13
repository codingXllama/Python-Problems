def BestFibN(userVal):
    myHash = {}
    
    if userVal in myHash:
        return myHash[userVal]
    else:
        myHash[userVal] = BestFibN(n - 1) + BestFibN(n - 2)
        return myHash[userVal]