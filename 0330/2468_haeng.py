#----------------------------------------------------------------------------------------#
def find(x,y):        #주변체크

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for d in range(4):
        X= x+dx[d]
        Y= y+dy[d]
        if 0<=X<N and 0<=Y<N and NN[Y][X] != '@' and visited[Y][X] == False:
            ST.append([X,Y])
            visited[Y][X] = True
    while ST:
        AA=ST.pop(0)
        find(AA[0],AA[1])

#----------------------------------------------------------------------------------------#


import copy
import sys
sys.setrecursionlimit(10 ** 5)

N=int(input())
Nlist=[]

maxN=0
for _ in range(N):
    A = list(map(int,input().split()))
    Nlist.append(A)

    if max(A) > maxN:
        maxN=max(A)

result=0
for i in range(maxN+1):
    NN = copy.deepcopy(Nlist)           #리스트복사해서 침수하는곳 '@' 변경
    for y in range(N):
        for x in range(N):
            if NN[y][x] <= i:
                NN[y][x] = '@'
    cnt=0
    visited = [[False] * N for _ in range(N)]
    for y in range(N):                                 #안전한영역 찾기
        for x in range(N):
            if NN[y][x] != '@' and visited[y][x] == False:
                ST=[]
                find(x,y)
                cnt += 1
    if cnt > result:
        result = cnt
print(result)