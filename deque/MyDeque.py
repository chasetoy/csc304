class Node:
    def __init__(self, item=0):
        self.prev = self.next = None
        self.item = item


class MyDeque:
    def __init__(self):
        self.head = self.tail = None
    def __str__(self):
        pstr = "["
        current = self.head
        while current !=  None:
            if pstr == "[":
                pstr += str(current.item)
                pstr += ", "
            elif current.next == None:
                pstr = pstr + str(current.item)
            else:
                pstr = pstr  + str(current.item) + ", "
            current = current.next
        pstr += "]"
        return pstr
    def isEmpty(self):
        return self.head is None and self.tail is None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    def addFront(self,item):
        if self.head == None:
            nu = Node(item)
            self.head = self.tail = nu
        else:
            oldHead = self.head
            self.head = Node(item)
            oldHead.prev = self.head
            self.head.next = oldHead
    def addRear(self,item):
        if self.tail == None:
            nu = Node(item)
            self.head = self.tail = None
        else:
            oldTail = self.tail
            self.tail = Node(item)
            oldTail.next = self.tail
            self.tail.prev = oldTail
    def removeFront(self):
        if self.head == None:
            pass
        elif self.head == self.tail:
            remove = self.head
            temp = remove.item
            self.head = self.tail = None
            return temp
        else:
            temp = self.head.item
            oldHead = self.head
            self.head = self.head.next
            self.head.prev = None
            oldHead.next = None
            oldHead = None
            return temp
    def removeRear(self):
        if self.tail == None:
            pass
        elif self.head == self.tail:
            remove = self.head
            temp = remove.item
            self.head = self.tail = None
            return temp
        else:
            temp = self.tail.item
            oldTail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            oldTail.prev = None
            oldTail = None
            return temp
