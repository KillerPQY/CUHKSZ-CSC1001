class Node:
    def __init__(self, element, pointer=None):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def __len__(self):
        self.size = self.recursive_count(self.head)
        return self.size

    def recursive_count(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.recursive_count(node.pointer)
        

if __name__ == '__main__':
    l = SinglyLinkedList()
    l.insert(2)
    l.insert(1)
    l.insert(0)
    print("The number of nodes is %d" % l.recursive_count(l.head))
