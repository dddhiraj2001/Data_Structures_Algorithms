class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self) -> str:
        x = self.head
        t_str = ""
        while x.next is not None:
            t_str+=f"{str(x.value)}->"
            x = x.next
        t_str+=str(x.value)
        return t_str
    

    def append(self,value):
        temp_node = Node(value)
        if self.head is None:
            self.head = temp_node
            self.tail = temp_node
        else:
            x = self.head
            while x.next is not None:
                x = x.next
            x.next = temp_node
            self.tail = temp_node
        self.length+=1
    
    def prepend(self,value):
        temp_node = Node(value)
        if self.head:
            temp_node.next = self.head
            self.head = temp_node
        else:
            self.head = temp_node
            self.tail = temp_node
        self.length+=1
    
    def insert(self,index,value):
        temp_node = Node(value)
        loop_node = self.head
        if index==0:
            self.prepend(value)
        else:
            for _ in range(index-1):
                loop_node = loop_node.next
            temp_node.next = loop_node.next
            loop_node.next=temp_node
        self.length+=1

    def traverse(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next
    
    def search(self,value):
        curr_node = self.head
        index=0
        while curr_node:
            if curr_node.value==value:
                return True,index
            curr_node = curr_node.next
            index+=1
        return False,index

    def get(self,index):
        curr_node = self.head
        if index<0 or index >=self.length:
            return None
        if index == 0:
            return curr_node
        else:
            for _ in range(index):
                curr_node=curr_node.next
            return curr_node
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        else:
            return False
    
    def pop(self):
        temp_node = self.head
        self.head = temp_node.next
        temp_node.next=None
        return temp_node.value
    def popend(self):
        
        y=self.head
        while y.next is not self.tail:
            y=y.next
        self.tail = y
        y.next=None
    
    def remove(self,index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node

    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0
        

        




    

my_linked_list = linked_list()
my_linked_list.prepend(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(30)
my_linked_list.append(30)
my_linked_list.append(30)
my_linked_list.prepend(10)
my_linked_list.prepend(100)
my_linked_list.insert(0,50)
my_linked_list.prepend(2)
print(my_linked_list.search(10))
my_linked_list.traverse()
print(my_linked_list)
my_linked_list.remove(2)
print(my_linked_list)

print(my_linked_list.pop())
print(my_linked_list)
my_linked_list.remove(2)
my_linked_list.delete_all()
print(my_linked_list)

