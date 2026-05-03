t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    # Convert to 0-based indexing for easier handling
    p = [x - 1 for x in p]
    
    found = False
    for i in range(n):
        if p[p[i]] == i:  # Check for 2-cycle: i -> p[i] -> i
            found = True
            break
    
    if found:
        print(2)
    else:
        print(3)