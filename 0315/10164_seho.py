def find_way(start_,end_):
    ## 시작점에 끝점까지 경우의수 찾아가기.
    for row in range(start_[0],end_[0]+1):
        for col in range(start_[1],end_[1]+1):
            if board[row][col] == 0:
                if row - 1 >= 0:
                    board[row][col] += board[row-1][col]
                if col - 1 >= 0:
                    board[row][col] += board[row][col-1]
    ## 다돌면 answer에 곱해줌. 
    global answer
    answer *= board[end_[0]][end_[1]]

n,m,k = map(int,input().split())
## 격자생성
board = [[0]*m for _ in range(n)]
answer = 1
## 좌 상 변에 좌표들 1로 채우기
## 중딩때인가 했던 창의력문제풀기가 풀이법.
for row in range(n):
    board[row][0] = 1
for col in range(m):
    board[0][col] = 1

## 중간좌표 구하기
mid_row,mid_col = 0,0
if k:
    mid_row = (k-1)//m
    mid_col = (k-1)%m

## 중간좌표가 있다면,
if mid_row or mid_col:
    ## 길찾기 함수 2번
    find_way([0,0],[mid_row,mid_col])
    for row in range(mid_row,n):
        board[row][mid_col] = 1
    for col in range(mid_col,m):
        board[mid_row][col] = 1
    find_way([mid_row,mid_col],[n-1,m-1])
else:
    ## 없으면 한번
    find_way([0,0],[n-1,m-1])
print(answer)


