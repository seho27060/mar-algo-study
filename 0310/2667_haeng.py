N=int(input())
Nlist=[]
for _ in range(N):
    Nlist.append(list(map(int,input())))

#-----------------------------------------------------------
ST=[]
def number(a,b,c):
    global cnt
    cnt += 1
    for i in range(4):
        X = a + dx[i]
        Y = b + dy[i]
        if 0<=X<N and 0<=Y<N and Nlist[Y][X] == 1:
            ST.append([X,Y])
            Nlist[Y][X] = c
    while ST:
        A = ST.pop()
        number(A[0],A[1],c)

#-----------------------------------------------------------


dx=[1,-1,0,0]
dy=[0,0,1,-1]
num=2                   #단지번호 1과 집이있는곳 1이 겹치면 안되서 visited 따로 안만들고 그냥 2부터 시작
result=[]
for y in range(N):
    for x in range(N):
        if Nlist[y][x] == 1:
            cnt=0
            Nlist[y][x]=num
            number(x,y,num)
            result.append(cnt)
            num += 1

result.sort()            #오름차순으로 정렬
print(num-2)             #처음 2부터시작했고, 위 for문 마지막에 의미없는 +1이 있기때문에 -2
for i in result:
    print(i)