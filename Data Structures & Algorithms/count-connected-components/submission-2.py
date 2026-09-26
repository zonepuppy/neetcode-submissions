class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # step 1 build adjacency list  
        visited = set()
        component = 0
        # create visited set
        # step 2, in outer loop, iterate over each node 
        def dfs(node):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
            

        for node in range(n):
            if node not in visited:
                component += 1 
                dfs(node)
        return component