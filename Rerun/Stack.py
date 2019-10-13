class Stack:
    def __init__(self):
        self.myStack = []
        
    def PushItem(self, val):
        self.myStack.append(val)
    
    def PopItem(self):
        return self.myStack.remove()

    def isEmpty(self):
        return self.myStack == []
        
    def ViewStack(self):
        return self.myStack

    def FindMax(self):
        maxItem=0
        for item in self.myStack:
            if item > maxItem:
                maxItem=item
        return maxItem




#Testing the class
myStack = Stack()
myStack.PushItem(10)
myStack.PushItem(11)
myStack.PushItem(21)
print("The max Item in the stack is: {}".format(myStack.FindMax()))

print(myStack.ViewStack())
