class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        visit = set()

        queue.append((0, 0))
        visit.add((0, 0))

        length = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length

                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0
                    or r + dr == rows or c + dc == cols
                    or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1

        return -1
