class Solution(object):
    def maximumDetonation(self, bombs):
        n = len(bombs)
        
        # Build graph
        graph = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i != j:
                    xj, yj, _ = bombs[j]
                    if (xi - xj)**2 + (yi - yj)**2 <= ri**2:
                        graph[i].append(j)
        def dfs(node, visited):
            visited.add(node)
            count = 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count += dfs(neighbor, visited)
            return count
        
        # Try each bomb
        max_bombs = 0
        for i in range(n):
            max_bombs = max(max_bombs, dfs(i, set()))
        
        return max_bombs