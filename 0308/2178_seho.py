import sys
## 재귀깊이를 버티질 못하니 깊이 늘려주기.
sys.setrecursionlimit(100*100)

n,m = map(int,input().split())
## 문자열로 입력됨, 문자열은 수정이 안되므로 수정가능하게 리스트로 받아 저장.
lst = [list(input()) for _ in range(n)]

## bfs
## 0,0 부터 출발. n-1,m-1 도착점.
## 재귀로 구현.
def bfs(get_):
    global n,m,lst
    ## 빈 리스트 선언
    queue = []
    ## 탐색기준이 될 get_ 순회
    for now in get_:
        ## 탐색 방향을 상하좌우 4개방향, (0,0)에서 (n-1,m-1)로 향하므로, 하 - 우 - 좌 - 상 순서로 탐색.
        for i in [(1,0),(0,1),(-1,0),(0,-1)]:
            ## 탐색하려는 좌표가 범위내에 있으며, 갈수 있는 지점이라면,
            if (0 <= now[0] + i[0] < n and 0 <= now[1] + i[1] < m) and (lst[now[0]+i[0]][now[1]+i[1]] == "1"):
                ## 지나온 길은 시작점부터 걸리는 거리를 대입했으므로, 탐색하려는 좌표에 탐색기준이 되는 좌표의 값에 1을 더해준다.
                lst[now[0]+i[0]][now[1]+i[1]] = lst[now[0]][now[1]] + 1
                ## 다음 탐색기준이 될 좌표 추가.
                queue.append([now[0]+i[0],now[1]+i[1]])
    ## 다음 탐색기준이 될 좌표가 있다면,
    if queue:
        ## bfs를 재귀 실행. for을 활용하여 순회하므로, FIFO가 구현됨.
        bfs(queue)

lst[0][0] = 0
bfs([[0,0]])
print(lst[n-1][m-1]+1)