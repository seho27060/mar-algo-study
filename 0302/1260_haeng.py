N,M,V = map(int,input().split())
Nlist=[]
for _ in range(M):
    Nlist.append(list(map(int,input().split())))

NN=[[] for _ in range(N+1)]
for i in range(M):
    NN[Nlist[i][0]].append(Nlist[i][1])
    NN[Nlist[i][1]].append(Nlist[i][0])
for i in range(N+1):
    NN[i].sort()


#---------------------------------------------------------------------------------------------------------
def DFS(X):
    result.append(X)
    visited[X] = True
    for i in NN[X]:
        if visited[i] == False:
            DFS(i)

#---------------------------------------------------------------------------------------------------------
def BFS(X):
    visited[X] = True
    ST=[]
    ST.append(X)
    while ST:
        t = ST.pop(0)
        result.append(t)
        visited[t] = True
        for j in NN[t]:
            if visited[j] == False and j not in ST:
                ST.append(j)
#---------------------------------------------------------------------------------------------------------



visited=[False]*(N+1)
result=[]
DFS(V)
print(*result)


visited=[False]*(N+1)
result=[]
BFS(V)
print(*result)