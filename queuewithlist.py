class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isempty(self):
        if self.items==[]:
            return True
        else:
            return False
    
    def enque(self,value):
        self.items.append(value)
        return "The element is appened at the end of the list"
    
    def deque(self):
        if self.isempty():
            return "There is no element in the list"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isempty():
            return "There is no element in the list"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None
    
    

customQueue = Queue()
customQueue.enque(1)
customQueue.enque(2)
customQueue.enque(3)
print(customQueue.peek())
customQueue.delete()
print(customQueue)    
