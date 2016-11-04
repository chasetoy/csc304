class TreeNode:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.parent = self.leftChild = self.rightChild = None

class BinarySearchTree:
    def __init__(self, rootKey = None, rootValue = None):
        if rootKey == None:
            self.root = None
        else:
            self.root = TreeNode(rootKey, rootValue)
    def put(self,key,value):
        if key<self.key:
            if self.leftchild == None:
                self.leftchild=TreeNode(key,value)
            else:
                self.leftchild.put(key,value)
        elif key > self.key:
            if self.rightchild == None:
                self.rightchild=TreeNode(key,value)
            else:
                self.rightchild.put(key,value)


    def get(self,key):
        if key<self.key:
            if self.leftchild==None:
                raise KeyError("Error: insert error message here from slides")
            else self.leftchild.get(key)
        elif key>self.key:
           if self.rightchild==None:
                raise KeyError("Error: insert error message here from slides")
            else self.rightchild.get(key) 
        else:
            return self.value
                
