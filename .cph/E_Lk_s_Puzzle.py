n, m = map(int, input().split())
grid = [input().strip() for i in range(n)]
visited = [[False] * m for i in range(n)]
dir = [(0, 1), (-1, 0), (1, 0), (0, -1)]

def dfs(x, y, parent_x, parent_y, depth, color):
    visited[x][y] = True
    
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if grid[nx][ny] != color:
            continue
        
        if nx == parent_x and ny == parent_y:
            continue
        
        if visited[nx][ny]:
            if depth + 1 >= 4:
                return True
            continue
        
        if dfs(nx, ny, x, y, depth + 1, color):
            return True
    
    return False  
found = False
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, -1, -1, 1, grid[i][j]):
                found = True
                break
    if found:
        break

print("Yes" if found else "No")