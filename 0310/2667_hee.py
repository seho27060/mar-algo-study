from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)] # 지도
visited = [[False]*N for _ in range(N)]
lst = [] # 단지 정보
D = [(1,0), (-1,0), (0,1), (0,-1)]

for y in range(N):
    for x in range(N):
        if arr[y][x] == '1' and not visited[y][x]:
            temp = 0 # 하나의 단지에 포함된 집의 수
            ST = deque([[x,y]])
            visited[y][x] = True
            while ST: # bfs
                s = ST.popleft()
                temp += 1
                for d in D:
                    nx = s[0] + d[0]
                    ny = s[1] + d[1]
                    if -1 < nx < N and -1 < ny < N and not visited[ny][nx] and arr[ny][nx] == '1':
                        ST.append([nx, ny])
                        visited[ny][nx] = True
            lst.append(temp)
lst.sort()
print(len(lst))
for i in lst : print(i)

