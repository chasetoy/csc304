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

    def delete(self, key):
        if self.key == key:
            if self.leftChild == None and self.rightChild == None:
                if self.parent.leftChild == self:
                    self.parent.leftChild = None
                else:
                    self.parent.rightChild = None
            else:
                succ = self.successor()
                if succ is not None:
                    if succ == self.parent:
                        self.parent.leftChild = self.leftChild
                        self.leftChild.parent = self.parent
                    else:
                        self.key = succ.key
                        self.value = succ.value
                        succ.delete(succ.key)
                else: #No successor. Use predecessor
                    pred = self.predecessor()
                    if pred == self.parent:
                        self.parent.rightChild = self.rightChild
                        self.rightChild.parent = self.parent
                    else:
                        self.key = pred.key
                        self.value = pred.value
                        pred.delete(pred.key)
        elif self.key > key:
            if self.leftChild is None:
                raise KeyError("Key %s not found." % str(key))
            else: self.leftChild.delete(key)
        else: #self.key < key
            if self.rightChild is None:
                raise KeyError("Key %s not found." % str(key))
            else: self.rightChild.delete(key)



    def get(self,key):
        if key<self.key:
            if self.leftchild==None:
                raise KeyError("Error: insert error message here from slides")
            else:
                self.leftchild.get(key)
        elif key>self.key:
           if self.rightchild==None:
                raise KeyError("Error: insert error message here from slides")
           else:
               self.rightchild.get(key)
        else:
            return self.value



def main():
    bst=BinarySearchTree()
    d = {}
    with open("test.txt") as f:
        for line in f:
            for row in f:
                a=[entry.strip() for entry in row.split(' ')] #creates a list of each of the values from each line
                if a[0] == 'm':
                    #bst.put(a[1],a[2]) #this deletes the pair from the BST
                    d[a[1]] = a[2]     #this deletes the pair from the dictionary
                if a[0] == 'd':
                    #bst.delete(a[1], a[2]) #this deletes the pair from the BST
                    del d[a[1]]            #this deletes the pair from the dictionary
                if a[0] == 'w':
                    #bst.delete(a[1], a[2]) #this deletes the pair from the BST
                    del d[a[1]]            #this deletes the pair from the dictionary
                if a[0] == 'Exit': #checking for the exit parameter
                    print("The remaining couples are : ", d)

main()
