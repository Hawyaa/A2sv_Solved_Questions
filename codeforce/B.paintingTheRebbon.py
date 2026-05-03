t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    
    if k >= n:
        print("NO")
        continue
    
    max_freq = (n + m - 1) // m
    
    if max_freq < n - k:
        print("YES")
    else:
        print("NO")