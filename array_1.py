class my_array:
    def __init__(self) -> None:
        self.length = 0
        self.data = {}
    
    def get(self,index):
        return self.data[index]
    
    def __str__(self) -> str:
        return f"{self.length},{self.data}"

    def push(self,item):
        self.data[self.length]=item
        self.length+=1
        return self.length
    
    def pop(self):
        del self.data[self.length-1]
        self.length-=1
    
    def delete(self,index):
        if self.length==0:
            return "empty array"
        x = self.data[index]
        self.shiftitems(index)
        
    def shiftitems(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1




x = my_array()
x.push('HI')
x.push('YOU')
x.push('!')
x.delete(0)
x.push('!!')
x.push('!!!')
x.delete(3)
x.delete(0)
x.delete(0)
x.delete(0)
x.delete(0)
x.delete(0)
x.delete(0)
x.delete(0)
print(x)