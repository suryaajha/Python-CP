class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_end(self, val):
        self.size += 1
        node = Node(val)
        if self.head == None:
            self.head = self.tail = node 
            return 
        node.prev = self.tail
        self.tail = node 
        
    def remove_first(self):
        size -= 1
        val = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return val 
    
class LRUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        self.ll = DoublyLL()
        self.ll_map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in ll_map:
            return kv[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.kv[key] = value
        if self.ll.size >= self.capacity:
            val = self.ll.remove_first()
            del self.ll_map[val]
        self.ll.add_at_end(key)
        self.ll_map[key] = self.ll.tail
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)