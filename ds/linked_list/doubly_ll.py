class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        # Setup dummyy head and tail node
        self.head = Node(-1)
        self.tail = Node(-1)
        # head.next point to tail and tail.prev points to head
        self.head.next = self.tail
        self.tail.prev = self.head

        # initial size is 0
        self.size = 0

    def append(self, val):
        self.size += 1
        node = Node(val, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        
    def delete(self, node):
        self.size -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

    def __repr__(self):
        result =[]
        temp = self.head.next
        while temp.next:
            result.append(temp.val)
            temp = temp.next
        return str(result)

    def __len__(self):
        return self.size

            
def main():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)

    print(dll)
    print(dll.size)
    dll.delete(dll.head.next.next.next)
    print(dll.size)
    print(dll)

if __name__ == '__main__':
    main()