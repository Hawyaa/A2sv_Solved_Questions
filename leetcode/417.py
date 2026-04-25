class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, ocean_set, prev_height):
            """DFS to mark all cells that can reach the ocean"""

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in ocean_set or
                heights[r][c] < prev_height):
                return
            ocean_set.add((r, c))
            
            dfs(r + 1, c, ocean_set, heights[r][c])
            dfs(r - 1, c, ocean_set, heights[r][c])
            dfs(r, c + 1, ocean_set, heights[r][c])
            dfs(r, c - 1, ocean_set, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])  
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])  
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])  
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])  
        
        # Find cells that can reach both oceans
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        
        return result