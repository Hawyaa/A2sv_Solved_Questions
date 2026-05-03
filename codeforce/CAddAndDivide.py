t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = 10**9
    for add in range(0, 100):
        nb = b + add
        if nb == 1:
            continue
        cnt = add
        ta = a
        while ta > 0:
            ta //= nb
            cnt += 1
        ans = min(ans, cnt)
    print(ans)