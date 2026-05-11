class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(currNode):
            for neighbor in adj[currNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        res = 0
        for currNode in range(n):
            if not visited[currNode]:
                visited[currNode] = True
                res+=1
                dfs(currNode)
        return res