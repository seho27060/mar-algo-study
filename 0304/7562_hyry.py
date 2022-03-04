# recursionerror 아니면 메모리초과
# dfs 재귀

import sys
input = sys.stdin.readline

def dfs(board, sR, sC, cnt):

    global minCnt

    D = ((-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1))

    ST = [(sR, sC)]
    board[sR][sC] = 1

    while ST:
        currR, currC = ST.pop()
        board[currR][currC] = 1 # 이게 지금 필요한지 안 필요한지 모르겠네
        cnt += 1 #맨 처음은 이동 횟수에 포함되면 안 되니 맨 처음 cnt = -1

        if cnt >= minCnt: return

        if currR == gR and currC == gC:
            if minCnt > cnt:
                minCnt = cnt
            return

        for dr, dc in D:
            newR = currR + dr
            newC = currC + dc

            if 0 <= newR < I and 0 <= newC < I and board[newR][newC] == 0:
                board[newR][newC] = 1
                dfs(board, newR, newC, cnt)
                board[newR][newC] = 0


T = int(input())
for _ in range(T):
    I = int(input())
    sR, sC = map(int, input().split())
    gR, gC = map(int, input().split())

    board = [[0] * I for _ in range(I)]
    minCnt = 1e10

    dfs(board, sR, sC, -1)

    print(minCnt)


# bfs로 풀기

import sys
input = sys.stdin.readline

def bfs():

    D = ((-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1))
    Q = [(sR, sC)]
    visited = [[0] * I for _ in range(I)]

    visited[sR][sC] = 1

    while Q:
        currR, currC = Q.pop(0)
        if currR == gR and currC == gC:
            return visited[currR][currC]

        for dr, dc in D:
            newR = currR + dr
            newC = currC + dc

            if 0 <= newR < I and 0 <= newC < I and visited[newR][newC] == 0:
                Q.append((newR, newC))
                visited[newR][newC] = visited[currR][currC] + 1


T = int(input())
for _ in range(T):
    I = int(input())
    sR, sC = map(int, input().split())
    gR, gC = map(int, input().split())

    board = [[0] * I for _ in range(I)]
    print(bfs() - 1)