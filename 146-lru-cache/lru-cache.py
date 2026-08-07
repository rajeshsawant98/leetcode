class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key 
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node: ListNode):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: ListNode):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.next = nxt 
        node.prev = prev
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            Node = self.cache[key]

            self.remove(Node)
            self.insert(Node)
            return Node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            Node = self.cache[key]
            self.remove(Node)
        NewNode = ListNode(key,value)
        self.cache[key] = NewNode
        self.insert(NewNode)

        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)