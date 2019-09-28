class Stack:
    def __init__(self):
        self.myStack = []
        
    #Creating the push operation
    def Push(self, val):
        self.myStack.append(val)

    #Creating the Pop operation
    def Pop(self):
        return self.myStack.pop()
    
    #checking if the stack is empty
    def isEmpty(self):
        return self.myStack == []
        
    #viewing the Stack
    def ViewStack(self):
        return self.myStack

    

def ReverseString(stack, str):
    
    #pushing items onto the stack
    for item in str:
        stack.Push(item)
        #Popping the items from the stack and storing that value in a empty list
        revList=[]
        revList+=stack.Pop()
    
    return revList



myStack = Stack()
print(ReverseString(myStack,"hello"))