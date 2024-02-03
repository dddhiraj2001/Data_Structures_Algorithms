class stack:
    def __init__(self,max_size):
        self.maxSize = max_size
        self.list=[]
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
        

customStack = stack(4)
print(customStack.isempty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
    
   

        