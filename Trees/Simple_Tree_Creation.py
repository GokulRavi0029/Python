#creation of node
class node():
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    #function for insertion of data into tree
    def insertdata(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insertdata(data)
            elif data > self.data:
                if self.right is None:
                    self.right=node(data)
                else:
                    self.right.insertdata(data)
        else:
            self.data=data
    
    #function to print tree
    def printnode(self):
        res = []
        if self.left:
            self.left.printnode()
        print(self.data),
        if self.right:
            self.right.printnode()

# used the insert method to add nodes
root = node(12)
root.insertdata(6)
root.insertdata(14)
root.insertdata(3)
root.insertdata(4)
root.printnode()
