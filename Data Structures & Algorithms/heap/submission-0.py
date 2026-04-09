class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        self.heap[1] = self.heap.pop()
        i = 1

        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) 
            and self.heap[2 * i + 1] < self.heap[2 * i] 
            and self.heap[i] > self.heap[2 * i + 1]):
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = temp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = temp
                i = 2 * i
            else:
                break
        return res

    def top(self) -> int:
        if len(self.heap) < 2:
            return -1 
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        #append the 0th index value
        self.heap = self.heap + nums

        cur = (len(self.heap) - 1) // 2

        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) 
                and self.heap[2 * i  + 1] < self.heap[2 * i] 
                and self.heap[i] > self.heap[2 * i + 1]):
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = temp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = temp
                    i = 2 * i
                else:
                    break
            cur -= 1