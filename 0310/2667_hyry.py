
def dfs(apart, row, col):
    global danji

    ST = [(row, col)]
    cnt = 0
    apart[row][col] = '0'

    while ST:
        currR, currC = ST.pop()
        cnt += 1

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR = currR + dr
            newC = currC + dc
            if 0 <= newR < N and 0 <= newC < N and apart[newR][newC] =='1':
                ST.append((newR, newC))
                apart[newR][newC] = '0'

    danji.append(cnt)

#--------------------------------------------

N = int(input())
apart = [list(input()) for _ in range(N)]

danji = []

for row in range(N):
    for col in range(N):
        if apart[row][col] == '1':
            dfs(apart, row, col)

#-----------------------------------------------
danji.sort()
print(len(danji))
print(*danji, sep='\n')


#######----------------- 다른 사람 코드 pj1002a + 수정

def dfs(graph, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        # return False
        return

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0

        dfs(graph, x + 1, y)
        dfs(graph, x - 1, y)
        dfs(graph, x, y + 1)
        dfs(graph, x, y - 1)


n = int(input())
graph = []
danji = []
num = 0

# for i in range(n):
#     graph.append(list(map(int, input())))
graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        cnt = 0
        if graph[i][j] == 1:
            dfs(graph, i, j)
            num += 1
            danji.append(cnt)

print(num)

danji.sort()
for i in danji:
    print(i)
