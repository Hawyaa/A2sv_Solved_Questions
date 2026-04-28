n=int(input())
ax,ay=map(int,input().split())
bx,by=map(int,input().split())
cx,cy=map(int,input().split())
if (ax-bx)*(ax-cx)>0 and (by-ay)*(cy-ay)>0:
    print("YES")
else:
    print("NO")