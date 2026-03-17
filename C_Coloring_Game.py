t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for j in range(1, n-1): 
        for k in range(j+1, n-1): 
            need = max(a[k] - a[j], a[n-1] - a[j] - a[k])
            lo, hi = 0, j
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] > need:
                    hi = mid
                else:
                    lo = mid + 1
            ans += j - lo
    for j in range(1, n-1):  
        need = a[n-1] - a[j]
        
        
        lo, hi = 0, j
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] > need:
                hi = mid
            else:
                lo = mid + 1
        ans += j - lo
    
    print(ans)