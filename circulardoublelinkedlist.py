class Node:
    def __init__(self,value):
        self.value = value
        self.previous = None
        self.next = None

class circularDoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def create(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.previous = new_node
        new_node.next = new_node
        return "The circular double linked list is created"
    
    def insert(self,value,index):
        if self.head==None:
            return "The CDLL does not exist"
        else:
            new_node = Node(value)
            if index==0:
                new_node.next = self.head
                new_node.previous = self.tail
                self.tail.next = new_node
                self.head.previous = new_node
                self.head = new_node
            elif index == 1:
                new_node.next = self.head
                new_node.previous = self.tail
                self.tail.next = new_node
                self.head.previous = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                for _ in range(index-1):
                    temp_node=temp_node.next
                new_node.next = temp_node.next
                new_node.previous = temp_node
                temp_node.next.previous = new_node
                temp_node.next=new_node
            return "The node has been successfully inserted"
    
    def traversal(self):
        if self.head is None:
            print("there is no node to traverse")
        else:
            temp_node = self.head
            while temp_node is not self.tail:
                print(temp_node.value)
                temp_node = temp_node.next
            print(temp_node.value)

    def reverse_traversal(self):
        if self.head is None:
            print("There is no node to traverse")
        else:
            temp_node=self.tail
            while temp_node is not self.head:
                print(temp_node.value)
                temp_node=temp_node.previous
            print(temp_node.value)
    
    def search(self,node_value):
        if self.head is None:
            print("there is no node to search")
        else:
            temp_node = self.head
            while temp_node:
                if self.head.value == node_value:
                    return temp_node.value
                if temp_node==self.tail:
                    return "The value does not exist"
                temp_node=temp_node.next
                
    def delete(self,location):
        if self.head is None:
            print("There is no node to delete")
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head.previous=None
                    self.head.next=None
                    self.head=None
                    self.tail=None 
                else:
                    self.head=self.head.next
                    self.head.previous = self.tail
                    self.tail.next=self.head
            elif location == 1:
                if self.head==self.tail:
                    self.head.previous=None
                    self.head.next=None
                    self.head=None
                    self.tail=None 
                else:
                    self.tail = self.tail.previous
                    self.tail.next = self.head
                    self.head.previous = self.tail
            else:
                curr_node = self.head
                for _ in range(location):
                    curr_node=curr_node.next
                curr_node.previous.next = curr_node.next
                curr_node.next.previous = curr_node.previous
            print("The node has been successfully deleted")
                




    
                
                    



circularDLL = circularDoubleLinkedList()
circularDLL.create(5)
circularDLL.insert(0,0)
circularDLL.insert(1,1)
circularDLL.insert(2,2)
print([node.value for node in circularDLL])
#circularDLL.traversal()
circularDLL.delete(-1)
print([node.value for node in circularDLL])

