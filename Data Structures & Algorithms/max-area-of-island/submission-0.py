class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_size = 0
        current_size = 0

        def dfs(r, c):
            if (r, c) in visited:
                return 
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 
            if grid[r][c] == 0:
                return 
            visited.add((r,c))
            nonlocal current_size, max_size
            
            current_size += 1
            max_size = max(current_size, max_size)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    current_size = 0
                    dfs(r, c)
        return max_size



