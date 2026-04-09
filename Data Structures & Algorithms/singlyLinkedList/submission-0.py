class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1
        
    def insertHead(self, val: int) -> None:
        curr = self.head.next
        newNode = Node(val)
        self.head.next = newNode
        newNode.next = curr
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        curr = self.tail
        newNode = Node(val)
        curr.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
