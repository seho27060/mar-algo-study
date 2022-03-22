def gram(x,g):
    global cnt
    if g < 500:
        return
    if x == N:
        cnt += 1
        return
    for c in range(N):
        if c in ST:
            continue
        ST.append(c)
        A = g + Nlist[ST[-1]] - K
        gram(x+1,A)
        ST.pop()


N,K=map(int,input().split())
Nlist=list(map(int,input().split()))

ST=[]
result=[]
cnt=0
for a in range(N):
    ST.append(a)
    g = 500 + Nlist[ST[-1]] -K
    gram(1,g)
    ST.pop()

print(cnt)