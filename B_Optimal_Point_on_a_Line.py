n=int(input())
s=list(map(int,input().split()))
if len(s)%2==1:
    print(s[n//2])
else:
    print(s[n//2-1])