n = int(input())
A, B = map(int, input().split())
N = int(input())

G = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(N):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

ST = [[A, 0]]
visited[A] = True
ans = 0

while ST: # dfs
    s = ST.pop()
    if s[0] == B:
        break
    for i in G[s[0]]:
        if not visited[i]:
            ST.append([i, s[1]+1])
            visited[i] = True
else: # break를 안 만나면 친척 관계 아님
    ans = -1

if ans == -1 :
    print(ans)
else :
    print(s[-1])


