class Graph:
    
    def __init__(self):
        self.adj_list = {} # src -> Set() of neighbors

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        
        self.adj_list[src].remove(dst)    
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque()

        queue.append(src)
        visited.add(src)


        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            for neighbor in self.adj_list.get(curr, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(curr)

        return False


