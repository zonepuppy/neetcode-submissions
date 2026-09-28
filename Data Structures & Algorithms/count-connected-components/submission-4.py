class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        component = 0
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

            
            return True

        for node in range(n):
            if node not in visited:
                dfs(node)
                component +=1

        return component