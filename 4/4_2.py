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
        return self.size

    def swap_element(self, n1, n2):
        n1.element, n2.element = n2.element, n1.element

    def quick_sort(self, node, end=None):
        if node != end:
            p1, p2 = node, node.pointer
            while p2 is not None:
                if p2.element < node.element:
                    p1 = p1.pointer
                    self.swap_element(p1, p2)
                p2 = p2.pointer
            self.swap_element(p1, node)
            self.quick_sort(node, p1)
            self.quick_sort(p1.pointer, end)
        return self.head

    def print_all_nodes(self):
        node = self.head
        while node:
            print(node.element, end=' ')
            node = node.pointer


if __name__ == '__main__':
    l = SinglyLinkedList()
    l.insert(6)
    l.insert(8)
    l.insert(3)
    l.insert(10)
    l.insert(2)
    l.insert(2)

    print(l.head)
    l.print_all_nodes()
    print()
    l.quick_sort(l.head)
    print(l.quick_sort(l.head))
    l.print_all_nodes()
