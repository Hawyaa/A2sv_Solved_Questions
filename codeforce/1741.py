t = int(input())

for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    
    n = m
    ans = 0
    possible = True
    
    size = 2
    while size <= n:
        for start in range(0, n, size):
            mid = start + size // 2 - 1
            min_right = min(p[mid+1:start+size])
            max_left = max(p[start:mid+1])
            
            if max_left > min_right:
                ans += 1
                p[start:mid+1], p[mid+1:start+size] = p[mid+1:start+size], p[start:mid+1]
                
                min_right = min(p[mid+1:start+size])
                max_left = max(p[start:mid+1])
                if max_left > min_right:
                    possible = False
                    break
        
        if not possible:
            break
        size *= 2
    
    for i in range(1, n):
        if p[i] < p[i-1]:
            possible = False
            break
    
    print(ans if possible else -1)