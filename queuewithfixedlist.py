class Queue:
    def __init__(self,size):
        self.items = [None for x in range(size)]
        self.max_size = size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start==0 and self.top==self.max_size-1:
            return True
        else:
            return False
    
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enque(self,value):
        if self.isFull():
            return "The queue is Full"
        else:
            if self.top==self.max_size-1:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value
            return "the Elemenet is inserted at the end of the Queue"
    
    def dequeue(self):
        if self.isempty():
            return "There is no element in the queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start=-1
                self.top=-1
            elif self.start == self.max_size-1:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return "The element has been removed from the queue"
    
    def peek(self):
        if self.isempty():
            return "There is no element in the queue"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = [None]*self.max_size
        self.start = -1
        self.top=-1
    
customQueue = Queue(3)
customQueue.enque(1)
customQueue.enque(2)
customQueue.enque(3)
print(customQueue.peek())
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)
print(customQueue.isFull())
customQueue.delete()
print(customQueue)


