class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)

class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next = new_node
        else:
            temp_node = self.tail
            new_node.next=temp_node.next
            temp_node.next = new_node
            self.tail = new_node
        self.length+=1
    
    def __str__(self):
        temp_node = self.head
        res=""
        while temp_node:
            res+=f"{temp_node.value}"
            if temp_node.next is not self.head:
                res+="->"
            temp_node=temp_node.next
            if temp_node is self.head:
                break
        return res
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1
    
    def insert(self,index,value):
        new_node = Node(value)
        temp_node=self.head
        if index==0:
            if self.head:
                new_node.next=self.head
                self.head = new_node
                self.tail.next=new_node
            else:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
        elif index==self.length:
            new_node.next=self.head
            self.tail.next=new_node
            self.tail=new_node
        else:
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
    def traversal(self):
        temp_node=self.head
        while temp_node:
            print(temp_node.value)
            temp_node=temp_node.next
            if temp_node is self.head:
                break
    def search(self,value):
        temp_node=self.head
        while temp_node:
            if temp_node.value==value:
                return True
            else:
                temp_node=temp_node.next
                if temp_node is self.head:
                    return False
    
    def get(self,index):
        if index>self.length:
            return False
        temp_node=self.head
        if index==0:
            return self.head.value
        for _ in range(index):
            temp_node=temp_node.next
        return temp_node


      


    

csLinkedList = circularLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
csLinkedList.prepend(30)
csLinkedList.insert(0,0)
csLinkedList.insert(0,100)
csLinkedList.traversal()
print(csLinkedList.search(100))

print(csLinkedList)
print(csLinkedList.get(3))


