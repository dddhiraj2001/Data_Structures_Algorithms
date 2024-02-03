class stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isempty(self):
        if len(self.list)==0:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def pop(self):
        if self.isempty():
            return "There is no element in the stack"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isempty():
            return "There is no element in the stack"
        else:
            return self.list[-1]

custom_stack = stack()
print(custom_stack.isempty())
custom_stack.push(1)
custom_stack.push(3)
print(custom_stack)
print(custom_stack.peek())
print(custom_stack)
    

        
        