n, k = map(int, input().split())
q = [n]
visited = [0]*100001
visited[n] = 1
while q:
    x = q.pop(0)
    d = [-1, 1, x]
    if x == k:
        print(visited[x]-1)
        break
    for i in range(3):
        nx = x+d[i]
        if 0<=nx<100001 and visited[nx] == 0:
            visited[nx] = visited[x]+1
            q.append(nx)