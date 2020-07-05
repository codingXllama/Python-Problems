class stack:
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def display(self):
        if not self.isEmpty():
            for item in self.items:
                print(item)
        return "\nSorry Stack is empty sorry,there's nothing to display!"


myStack = stack()
if myStack.isEmpty():
    myStack.push(1)
    myStack.push(33)
    myStack.push(2)

for x in range(3):
    myStack.pop()
print(myStack.display())
