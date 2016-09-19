class Node:
    def __init__(self, item=0):
        self.item = item
        self.prev = self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
    def addFirst(self, item):
        nu = Node(item)
        if self.head == None:
            self.head = self.tail = nu
        else:
            hp = self.head
            self.head = nu
            nu.next = hp
            hp.prev = nu
    def removeFirst(self):
        if self.head != None:
            rv = self.head.item
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                hp = self.head
                self.head = hp.next
                self.head.prev = None
                return rv
    def insertAfter(node, item):
        if node != None:
            nextn = node.next
            nu = Node(item)
            nu.prev = node
            nu.next = nextn
            node.next = nu
            if nextn != None:
                nextn.prev = nu
    def search(self, item):
        current = self.head
        while (current != None and current.item != item):
            current = current.next
        if current == None:
            return None
        else:
            return current
    def pop(self, node):
        if node != None:
            if node == self.head: self.removeFirst(node)
            elif node == self.tail: self.removeLast(node)
            else:
                np = node.prev
                nn = node.next
                np.next = node.next
                nn.prev = node.prev
