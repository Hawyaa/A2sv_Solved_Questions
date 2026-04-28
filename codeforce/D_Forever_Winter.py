t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    degree=[0]*(n+1)
    adj=[[] for _ in range(n+1)]
    for i in range(m):
        u,v=map(int,input().split())
        degree[u]+=1
        degree[v]+=1
        adj[u].append(v)
        adj[v].append(u)
    center=None
    for node in range(1,n+1):
        if degree[node]>1 and all(degree[nei]>1 for nei in adj[node]):
            center=node
            break
    x=degree[center]
    middle=adj[center][0]
    y=degree[middle]-1
    print(x,y)

