class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        level = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        def build_neighbor_list(i, j):
            neighbors = []
            if check_in_bounds(i + 1, j):
                neighbors.append((i + 1, j))
            if check_in_bounds(i, j + 1):
                neighbors.append((i, j + 1))
            if check_in_bounds(i - 1, j):
                neighbors.append((i - 1, j))
            if check_in_bounds(i, j - 1):
                neighbors.append((i, j-1))
            return neighbors


        def check_in_bounds(i, j):
            if i < 0 or i > len(grid) - 1:
                return False
            if j < 0 or j > len(grid[0]) - 1:
                return False
            if grid[i][j] == -1:
                return False
            return True

        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                i, j = queue.popleft()
                

                neighbor_list = build_neighbor_list(i, j)
                for i, j in neighbor_list:
                    if grid[i][j] == 2147483647:
                        grid[i][j] = level + 1
                        queue.append((i, j))
            level += 1

        return None
            
        
        

