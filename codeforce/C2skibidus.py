t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    last = -10**18
    possible = True
    
    for val in a:
        candidates = []
        if val >= last:
            candidates.append(val)
        
        # binary search for smallest b >= last + val
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if b[mid] >= last + val:
                hi = mid
            else:
                lo = mid + 1
        
        if lo < m:
            candidates.append(b[lo] - val)
        
        if not candidates:
            possible = False
            break
        
        last = min(candidates)
    
    print("YES" if possible else "NO")