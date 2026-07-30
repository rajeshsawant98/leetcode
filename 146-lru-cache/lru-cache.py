class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = Node
        Node.next, Node.prev = nxt, prev
    
    def delete(self, Node):
        prev, nxt = Node.prev, Node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]

"""

cache

 : (1,1)
4 : (4,4)

L ->  (3,3) -> (4,4) -> R
"""
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)