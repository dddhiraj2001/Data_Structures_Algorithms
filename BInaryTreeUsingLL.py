class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = BinaryTreeNode("Drinks")
leftChild = BinaryTreeNode("Hot")
rightChild = BinaryTreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return "it is none"
    else:
        cust_queue = []
        cust_queue.append(rootNode)
        while len(cust_queue)!=0:
            temp_node = cust_queue.pop(0)
            print(temp_node.data)
            if temp_node.leftChild:
                cust_queue.append(temp_node.leftChild)
            if temp_node.rightChild:
                cust_queue.append(temp_node.rightChild)

def search(rootNode,value):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        cust_queue = []
        cust_queue.append(rootNode)
        while len(cust_queue)!=0:
            temp_node = cust_queue.pop(0)
            if temp_node.value == value:
                return "Success"
            if temp_node.leftChild:
                cust_queue.append(temp_node.leftChild)
            if temp_node.rightChild:
                cust_queue.append(temp_node.rightChild)
        return "Unsuccessful in the search of the binary tree"

def insert(rootNode,newNode):
    if rootNode is None:
        rootNode=newNode
    else:
        cust_queue = []
        cust_queue.append(rootNode)
        temp_node=None
        while len(cust_queue)!=0:
            temp_node = cust_queue.pop(0)
            if temp_node.leftChild==None:
                temp_node.leftChild=newNode
                return "Successfully inserted"
            if temp_node.rightChild==None:
                temp_node.rightChild=newNode
                return "Successfully inserted"
            if temp_node.leftChild:
                cust_queue.append(temp_node.leftChild)
            if temp_node.rightChild:
                cust_queue.append(temp_node.rightChild)

def getDeepestNode(rootNode):
    if rootNode is None:
        return 
    else:
        cust_queue = []
        cust_queue.append(rootNode)
        while len(cust_queue)!=0:
            temp_node = cust_queue.pop(0)
            if temp_node.leftChild:
                cust_queue.append(temp_node.leftChild)
            if temp_node.rightChild:
                cust_queue.append(temp_node.rightChild)
        return temp_node

def deleteDeepestNode(rootNode):
    if rootNode is None:
        return 
    else:
        x = getDeepestNode(rootNode)
        if rootNode==x:
            rootNode.data=None
        cust_queue = []
        cust_queue.append(rootNode)
        while len(cust_queue)!=0:
            temp_node = cust_queue.pop(0)
            if temp_node.leftChild:
                if temp_node.leftChild==x:
                    temp_node.leftChild=None
                    return
                cust_queue.append(temp_node.leftChild)
            if temp_node.rightChild:
                if temp_node.rightChild==x:
                    temp_node.rightChild=None
                    return
                cust_queue.append(temp_node.rightChild)
        return temp_node


def deleteBT(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None



       


deleteDeepestNode(newBT)
deleteDeepestNode(newBT)
deleteDeepestNode(newBT)
deleteBT(newBT)
levelOrderTraversal(newBT)





        
        

    

