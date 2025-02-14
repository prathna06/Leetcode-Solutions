from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        D = defaultdict(list)
        for u,v in connections:
            D[u].append((v,1))
            D[v].append((u,0))
        
        def dfs(node,parent):
            change = 0
            for neighbour,direction in D[node]:
                if neighbour != parent:
                    change += direction
                    change += dfs(neighbour,node)
            return change
        return dfs(0,-1)
        
      

        






