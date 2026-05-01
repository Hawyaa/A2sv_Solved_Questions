class Solution(object):
    def getAncestors(self, n, edges):
        # Build reverse graph (easier for finding ancestors)
        reverse_graph = [[] for _ in range(n)]
        for u, v in edges:
            reverse_graph[v].append(u)  # v has incoming edge from u
        
        ancestors = [set() for _ in range(n)]
        
        def dfs(anc, current):
            """DFS from 'current' to find all ancestors of 'anc'"""
            for parent in reverse_graph[current]:
                if parent not in ancestors[anc]:
                    ancestors[anc].add(parent)
                    dfs(anc, parent)
        
        # Find all ancestors for each node
        for i in range(n):
            dfs(i, i)
        
        return [sorted(anc) for anc in ancestors]