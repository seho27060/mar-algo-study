# dfs
def dfs(x, y):
    global num
    if x <0 or x >=n or y <0 or y >=n or grid[x][y] == '0':
        return
    grid[x][y] = '0'
    num += 1
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

n = int(input())
grid = [list(input()) for _ in range(n)]
count = 0
nums = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == '1':
            num = 0
            dfs(x, y)
            nums.append(num)
            count += 1
print(count)
nums.sort()
for nu in nums:
    print(nu)

# bfs
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
nums = []
q = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for x in range(n):
    for y in range(n):
        if arr[x][y] == '1' and visited[x][y] == 0:
            cnt += 1
            num = 1
            visited[x][y] = 1
            q.append([x, y])
            while q:
                a, b = q.pop(0)
                for i in range(4):
                    nx = a+dx[i]
                    ny = b+dy[i]
                    if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and arr[nx][ny] == '1':
                        visited[nx][ny] = 1
                        num += 1
                        q.append([nx, ny])
            nums.append(num)
print(cnt)
nums.sort()
for nu in nums:
    print(nu)