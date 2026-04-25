class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        color=[-1]*n
        def bfs(start):
            queue=deque([start])
            color[start]=0
            while queue:
                node=queue.popleft()
                cur_color=color[node]
                for nei in graph[node]:
                    if color[nei]==-1:
                        color[nei]=1-cur_color
                        queue.append(nei)
                    elif color[nei]==cur_color:
                        return False
            return True
        for i in range(n):
            if color[i]==-1:
                if not bfs(i):
                    return False
        return True

        