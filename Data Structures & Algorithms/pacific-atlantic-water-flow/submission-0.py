class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        visited_pacific = set()
        visited_atlantic = set()
        result = []

        def dfs(r, c, visited_set):
            # Out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # Already explored for this ocean
            if (r, c) in visited_set:
                return

            visited_set.add((r, c))

            # Reverse-flow search:
            # only move to a neighbor that is >= current height

            if r + 1 < rows and heights[r + 1][c] >= heights[r][c]:
                dfs(r + 1, c, visited_set)

            if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                dfs(r - 1, c, visited_set)

            if c + 1 < cols and heights[r][c + 1] >= heights[r][c]:
                dfs(r, c + 1, visited_set)

            if c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                dfs(r, c - 1, visited_set)

        # Pacific: top row + left column
        for r in range(rows):
            dfs(r, 0, visited_pacific)

        for c in range(cols):
            dfs(0, c, visited_pacific)

        # Atlantic: bottom row + right column
        for r in range(rows):
            dfs(r, cols - 1, visited_atlantic)

        for c in range(cols):
            dfs(rows - 1, c, visited_atlantic)

        # Cells reachable from BOTH oceans
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited_pacific and (r, c) in visited_atlantic:
                    result.append([r, c])

        return result