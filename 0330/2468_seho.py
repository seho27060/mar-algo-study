import copy
def findSafearea(rain,loc):
    global nxtBoard, n, result,moves

    stack = [loc]
    result += 1
    while stack:
        tmp = stack.pop()
        nxtBoard[tmp[0]][tmp[1]] = -1
        for move in moves:
            row = move[0] + tmp[0]
            col = move[1] + tmp[1]
            if 0 <= row < n and 0 <= col < n and nxtBoard[row][col] > rain:
                stack.append([row,col])

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer = 0

moves = [[0,1],[0,-1],[1,0],[-1,0]]
for rain in range(0,101):
    result = 0
    nxtBoard = copy.deepcopy(board)
    for row in range(n):
        for col in range(n):
            if nxtBoard[row][col] > rain:
                findSafearea(rain,[row,col])
    if answer < result:
        answer = result
print(answer)
##