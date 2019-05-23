class node():
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
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
            
    def printnode(self):
        if self.left:
            self.left.printnode()
        print(self.data),
        if self.right:
            self.right.printnode()
    
    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res
    def Preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.Preorder(root.left)
            res = res + self.Preorder(root.right)
        return res
    def Postorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res = res + self.Preorder(root.right)
            res.append(root.data)
        return res
            


root = node(12)
root.insertdata(6)
root.insertdata(14)
root.insertdata(3)
root.insertdata(4)

print(root.inorder(root))

root = node(12)
root.insertdata(6)
root.insertdata(14)
root.insertdata(3)
root.insertdata(4)
print(root.Preorder(root))

root = node(12)
root.insertdata(6)
root.insertdata(14)
root.insertdata(3)
root.insertdata(4)
print(root.Postorder(root))