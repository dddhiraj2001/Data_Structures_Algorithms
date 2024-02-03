class BinaryTree:
    def __init__(self,size):
        self.custom_list = [None]*size
        self.lastUsedIndex=0
        self.max_size = size
    
    def insertNode(self,value):
        if self.lastUsedIndex+1==self.max_size:
            return "The binary tree is full"
        self.custom_list[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return "The value has been successfully inserted"
    def search(self,value):
        for i in self.custom_list:
            if i == value:
                return "The value is found"
        return "The value is not found"
    
    def preOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return 
        print(self.custom_list[index])
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index+1)
    
    def inOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.inOrderTraversal(2*index)
        print(self.custom_list[index])
        self.inOrderTraversal(2*index+1)
    
    def postOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return 
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index+1)
        print(self.custom_list[index])
    
    def levelOrderTraversal(self,index):
        while index <= self.lastUsedIndex:
            print(self.custom_list[index])
            index+=1
            
    
    


newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))

# newBT.preOrderTraversal(1)
newBT.levelOrderTraversal(1)


