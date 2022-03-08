N = int(input())
cpt = [[] for _ in range(N+1)]
n = int(input())

for _ in range(n):
    A, B = map(int, input().split())
    cpt[A].append(B)
    cpt[B].append(A)
visited = [False] * (N+1)
ST = [1]
visited[1] = True
cnt = -1

while ST: #dfs
    s = ST.pop()
    cnt += 1

    for i in cpt[s]:
        if not visited[i]:
            ST.append(i)
            visited[i] = True
print(cnt)