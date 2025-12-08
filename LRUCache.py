# 146. LRU Cache
class Node:
    def __init__(self, key:int, value:int, next:"Node", prev:"Node"):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.map:dict[int, Node] = {}
        self.capacity = capacity
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, None)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node:Node) -> None:
        prevN = node.prev
        nextN = node.next
        prevN.next = nextN
        nextN.prev = prevN
    
    def insert(self, node:Node) -> None:
        prevN = self.right.prev
        prevN.next = node
        node.prev = prevN
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.map) == self.capacity:
                first = self.left.next
                self.map.pop(first.key)
                self.remove(first)
            node = Node(key, value, None, None)
            self.map[key] = node
            self.insert(node)
            