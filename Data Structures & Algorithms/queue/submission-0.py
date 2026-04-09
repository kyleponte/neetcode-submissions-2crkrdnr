class Deque:
    
    def __init__(self):
        self.q = deque()

    def isEmpty(self) -> bool:
        if len(self.q) == 0:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        self.q.append(value)

    def appendleft(self, value: int) -> None:
        self.q.appendleft(value)

    def pop(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q.pop()

    def popleft(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q.popleft()
