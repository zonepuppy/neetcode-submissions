class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i : [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        count = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in adj:
            if node not in visited:
                dfs(node)
                count += 1
        return count