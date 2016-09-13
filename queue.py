class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def main():


    q1 = Queue()

    q1.enqueue(4)
    print(q1.size())

    q1.enqueue(16)

    print(q1.isEmpty())
    print(q1.size())

    q1.dequeue()
    q1.dequeue()

    print(q1.isEmpty())
    print(q1.size())


main()

# This can be used in the real world situation of a bank and determining
# how many tellers are need to keep time between customer at a
# consistent rate ex. 1.5 minutes per customer