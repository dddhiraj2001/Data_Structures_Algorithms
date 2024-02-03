class Node:
    def __init__(self,value):
        self.previous = None
        self.next = None
        self.value = value

    def __str__(self):
        return f"{self.value}"

class doublelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.previous=self.tail
            self.tail=new_node
        self.length+=1
    
    def __str__(self):
        temp_node=self.head
        res=""
        while temp_node:
            res+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node is not None:
                res+= '<->'
        return res
    
    def prepend(self,value):
        temp_node = Node(value)
        if self.head is None:
            self.head=temp_node
            self.tail=temp_node
        else:
            temp_node.next=self.head
            self.head.previous = temp_node
            self.head=temp_node
        self.length+=1
    
    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node=temp_node.next
    def reverse_traversal(self):
        temp_node=self.tail
        while temp_node:
            print(temp_node.value)
            temp_node=temp_node.previous
    
    def search(self,target):
        temp_node = self.head
        index=0
        while temp_node:
            if temp_node.value==target:
                return True,index
            temp_node=temp_node.next
            index+=1
        return False,-1
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index<self.length//2:
            curr_node = self.head
            for _ in range(index):
                curr_node=curr_node.next
        else:
            curr_node=self.tail
            for _ in range(self.length-1,index,-1):
                curr_node=curr_node.previous
        return curr_node
    
    def set(self,index,value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
        else:
            return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            print("Index out of bounds")
            return 
        temp_node = Node(value)
        if index==0:
            self.prepend(value)
            return 
        elif index==self.length-1:
            self.append(value)
            return 
        priv_node = self.get(index-1)
        temp_node.next = priv_node.next
        temp_node.previous = priv_node
        priv_node.next.previous = temp_node
        priv_node.next = temp_node
        self.length+=1
    
    def pop_first(self):
        if self.head is None:
            return None
        temp_node = self.head
        if self.length==1:
            self.head=None
            self.tail=None
            
        else:
            self.head = self.head.next
            self.head.previous = None
            temp_node.next = None
        self.length-=1
        return temp_node
    
    def pop(self):
        if self.head is None:
            return None
        temp_node = self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            temp_node.previous = None
        self.length-=1
        return temp_node
    
    def remove(self,index):
        if index<0 and index>self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp_node = self.get(index)
        temp_node.previous.next = temp_node.next
        temp_node.next.previous = temp_node.previous
        temp_node.next=None
        temp_node.previous=None
        self.length-=1
        return temp_node
        

        
        
                



newDLL = doublelinkedlist()
newDLL.append(10)
newDLL.append(55)
newDLL.prepend(22)
newDLL.append(20)
newDLL.append(55)
newDLL.prepend(22)
newDLL.traverse()
newDLL.reverse_traversal()
print(newDLL.search(55))
print(newDLL)
newDLL.set(2,22)
newDLL.insert(3,33)
print(newDLL)
print(newDLL.pop_first())
newDLL.pop()
print(newDLL)
newDLL.remove(2)
print(newDLL)
newDLL.remove(0)
newDLL.remove(2)
print(newDLL)
    
