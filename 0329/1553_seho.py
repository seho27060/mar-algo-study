def backtracking(loc):
    global board, result, dominos, answer, moves
    for move in moves:
        row = loc[0] + move[0]
        col = loc[1] + move[1]
        if 0 <= row < 8 and 0 <= col < 7 and result[row][col] == -1:
            ## 도미노를 뒤집어서 매치되는 경우를 위함.
            ## 여기서 set을 안해줘서 128배가 많이 나왔다.
            findDomino =set(["".join([str(board[loc[0]][loc[1]]),str(board[row][col])]),"".join([str(board[row][col]),str(board[loc[0]][loc[1]])])])

            for findDomino1 in findDomino:
                ## dominos에 매치된 도미노가 있다면
                if dominos.get(findDomino1,0):
                    ## 경우의 수 기록을 위한 result에 대입하고
                    result[loc[0]][loc[1]] = int(findDomino1[0])
                    result[row][col] = int(findDomino1[1])
                    dominos[findDomino1] = 0
                    check = False
                    ## 그 다음 result의 빈 공간 탐색
                    for r in range(8):
                        for c in range(7):
                            if result[r][c] == -1:
                                check = True
                                nxtrow = r
                                nxtcol = c
                                break
                        if check:
                            break
                    ## 빈공간이 있다면 해당 좌표를 탐색하는 백트래킹
                    if check:
                        backtracking([nxtrow,nxtcol])
                    ## 없다면 경우의 가짓수 +1
                    else:
                        answer += 1
                    ## 백트래킹 과정을 위해 수정했던 좌표값 초기화시켜줌.
                    result[loc[0]][loc[1]] = -1
                    result[row][col] = -1
                    dominos[findDomino1] = 1

board = [list(map(int,input())) for _ in range(8)]
result = [[-1]*7 for _ in range(8)]
dominos = {}
answer = 0
## 좌표를 하나씩 이동해가면서 상하좌우를 탐색
## 딕셔너리 dominos에 매치된 도미노가 있는지 확인하고 있으면 넣고
## 다음 빈공간을 찾아 백트래킹한다.
moves = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(7):
    for j in range(i,7):
        dominos["".join([str(i),str(j)])] = 1

backtracking([0,0])
print(answer)