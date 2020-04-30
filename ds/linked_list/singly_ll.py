class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        # Setup dummyy head and tail node
        self.head = Node(-1)
        self.tail = None

        # initial size is 0
        self.size = 0

    def append(self, val):
        self.size += 1
        node = Node(val)
        if not self.tail: # If we have no elements
            self.head.next = node
        else:
            self.tail.next = node
        self.tail = node
        
    def delete(self, node_prev):
        self.size -= 1
        if node_prev.next is self.tail:
            self.tail = node_prev
        node_prev.next = node_prev.next.next

    def __repr__(self):
        result =[]
        temp = self.head.next
        while temp:
            result.append(temp.val)
            temp = temp.next
        return str(result)

    def __len__(self):
        return self.size
    
            
def main():
    dll = SinglyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)

    print(dll)
    print(dll.size)
    dll.delete(dll.head.next.next.next)
    dll.append(50)
    print(dll.size)
    print(dll)

if __name__ == '__main__':
    main()