class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * self.capacity

    def hash(self, key):
        return key % self.capacity 

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        node = self.map[index]

        if not node:
            self.map[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.map[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        node = self.map[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.map[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        newMap = [None] * newCapacity

        for node in self.map:
            while node:
                index = node.key % self.capacity
                if newMap[index] == None:
                    newMap[index] = Node(node.key, node.value)
                else:
                    newNode = newMap[index]
                    while newNode.next:
                        newNode = newNode.next
                    newNode.next = Node(node.key, node.value)
                node = node.next
        
        self.capacity = newCapacity
        self.map = newMap