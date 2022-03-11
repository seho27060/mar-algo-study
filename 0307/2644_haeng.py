N=int(input())
N1,N2 = map(int,input().split())
NN= int(input())
Ndict_up = {i:[] for i in range(N+1)}              
Ndict_down = {i:[] for i in range(N+1)}
Nlist=[]

for _ in range(NN):
    a,b=map(int,input().split())
    Nlist.append([a,b])
    Ndict_up[b].append(a)
    Ndict_down[a].append(b)

visited=[False for _ in range(N+1)]

ST=[]
def family(x, cnt):
    visited[x] = True
    if x == N2:
        global Y
        Y = cnt

    if len(Ndict_up[x]) > 0:
        for i in range(len(Ndict_up[x])):
            ST.append([Ndict_up[x].pop(),cnt+1])
    if len(Ndict_down[x]) > 0:
        for i in range(len(Ndict_down[x])):
            ST.append([Ndict_down[x].pop(),cnt+1])

    while ST:
        a = ST.pop(0)
        if visited[a[0]] == False:
            family(a[0],a[1])

Y = -1
cnt=0
family(N1, cnt)
print(Y)