## 파이썬, 파이파이에서는 최대 재귀깊이는 1000
## 문제에서 주어진 배추밭은 50*50 = 2500
## 모든 탐색을 한다고 하면 2500번의 재귀 실행.
## 재귀 깊이 늘려주기. --> 재귀깊이를 무작정 크게 늘려주면, 메모리가 많이 할당됨. 주의.
import sys
sys.setrecursionlimit(10**4)

def find_(row,col):
    global lst
    global m
    global n
    if lst[row][col] == 1:  ## 해당위치에 배추가 있다면, 방문했다는 의미로 0을 할당.
        lst[row][col] = 0
    else:                   ## 해당 위치에 배추가 없다면, return. dsf의 재귀 끝.
        return

    ## x,y 가 정해진 범위를 벗어나지 않는 한에 dfs 실행.
    if row - 1 >= 0:
        find_(row-1,col)
    if row + 1 < n:
        find_(row+1, col)
    if col - 1 >= 0:
        find_(row ,col-1)
    if col + 1 < m:
        find_(row, col +1 )

nums = int(input())

for i in range(nums):
    m,n,k = map(int,input().split())
    lst = [[0]*m for _ in range(n)] ## 전체 맵

    for j in range(k):
        x,y = map(int,input().split())
        lst[y][x] = 1   ## 배추가 있는 좌표에 1 할당.

    count = 0
    for row in range(n):
        for col in range(m):
            if lst[row][col] == 1:
                find_(row,col)  ## 맵을 순회하면서 배추가 있다면, 해당위치에서 dfs 실행.
                count += 1      ## 해당 위치에서 탐색을 시작하고 배추를 모두 뽑아버리므로
    print(count)                ## 다시 돌아올일 없음. count 증가하여 배추밭 개수 세기.