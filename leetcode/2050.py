from collections import defaultdict, deque

class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        
        # Build graph and indegree
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        
        # Queue for topological sort (Kahn's algo)
        q = deque()
        
        # Finish time for each node (1-indexed)
        finish_time = [0] * (n + 1)
        
        # Initialize: nodes with no prerequisites
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                finish_time[i] = time[i - 1]
        
        # Process in topological order
        while q:
            u = q.popleft()
            for v in graph[u]:
                # Update finish time of v based on predecessor u
                finish_time[v] = max(finish_time[v], finish_time[u] + time[v - 1])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        # Answer is the max finish time over all courses
        return max(finish_time[1:])