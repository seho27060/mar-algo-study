import sys

input = sys.stdin.readline

N = int(input())
p1, p2 = map(int, input().split())
M = int(input())

Adj = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    P, C = map(int, input().split())
    Adj[P].append(C)
    Adj[C].append(P)


# def bfs():
Q = []
visited = [0] * (N + 1)

Q.append(p1)
visited[p1] = 1 # 1을 넣고 시작하니까

while Q:
    currV = Q.pop(0)
    for v in Adj[currV]:
        if not visited[v]:
            Q.append(v)
            visited[v] = visited[currV] + 1

if visited[p2] == 0: print(-1)
else: print(visited[p2] - 1)