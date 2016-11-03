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
            
