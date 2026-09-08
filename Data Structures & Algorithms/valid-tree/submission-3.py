class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjacencyList = {i : [] for i in range(n)}

        for i in range(len(edges)):
                adjacencyList[edges[i][0]].append(edges[i][1])
                adjacencyList[edges[i][1]].append(edges[i][0])

        
        
        def dfs(node, parent):
            visited.add(node)

            for neighbor in adjacencyList[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for node in adjacencyList:
            if node not in visited:
                if dfs(node, None):
                    return False

        
        visited = set()
        start_node = next(iter(adjacencyList))
        dfs(start_node, None)
        if len(visited) != len(adjacencyList):
            return False

        return True



