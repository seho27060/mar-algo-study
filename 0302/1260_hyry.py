import sys
input = sys.stdin.readline


def dfs():
    ST, sRes = [], []
    ST.append(S)

    while ST:
        currV = ST.pop()
        if sVisited[currV] == False:
            sRes.append(currV)
            sVisited[currV] = True

            for v in sAdj[currV]:
                if not sVisited[v]:
                    ST.append(v)

    return sRes


def bfs():
    Q, qRes = [], []
    Q.append(S)
    qStored[S] = True

    while Q:
        currV = Q.pop(0)
        qRes.append(currV)

        for v in qAdj[currV]:
            if not qStored[v]:
                Q.append(v)
                qStored[v] = True

    return qRes

N, M, S = map(int, input().rstrip().split())

# 인접 리스트 생성
Adj = [[] for _ in range(N + 1)] # 0, 1 ~ N
for _ in range(M):
    v1, v2 = map(int, input().rstrip().split())
    Adj[v1].append(v2)
    Adj[v2].append(v1)
sAdj = [sorted(i, reverse=True) for i in Adj]
qAdj = [sorted(i) for i in Adj]

sVisited = [False] * (N + 1)
qStored = [False] * (N + 1)

print(*dfs())
print(*bfs())




