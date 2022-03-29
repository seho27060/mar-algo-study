def next():
    global ans
    for i in range(8):
        for j in range(7):
            if visited[i][j] == 0:
                dfs(i, j)
                return
    if len(domino) == 0:
        ans += 1
        return

def dfs(x, y):
    dx = [0, 1]
    dy = [1, 0]
    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<8 and 0<=ny<7 and visited[nx][ny] == 0:
            if arr[x][y]+arr[nx][ny] in domino:
                domino.remove(arr[x][y]+arr[nx][ny])
                visited[x][y] = 1
                visited[nx][ny] = 1
                next()
                visited[x][y] = 0
                visited[nx][ny] = 0
                domino.append(arr[x][y]+arr[nx][ny])

            elif arr[nx][ny]+arr[x][y] in domino:
                domino.remove(arr[nx][ny]+arr[x][y])
                visited[x][y] = 1
                visited[nx][ny] = 1
                next()
                visited[x][y] = 0
                visited[nx][ny] = 0
                domino.append(arr[nx][ny]+arr[x][y])

domino = ['00','01','02','03','04','05','06','11','12','13','14','15','16',
          '22','23','24','25','26','33','34','35','36','44','45','46','55','56','66']
arr = [list(input()) for _ in range(8)]
visited = [[0]*7 for _ in range(8)]
ans = 0
dfs(0,0)
print(ans)