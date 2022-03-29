def domino(x,y):                                #어짜피 6,1은 1,6이기 때문에 겹치지않은 짝으로 모두를 묶을수 있는지 확인
    global cnt
    if len(ST) == 27:                           #56칸에서 27칸을 사용했고
        dx=[1,-1,0,0]                           #마지막 남은 두 False가 붙어있고 사용하지 않은 짝이면 cnt+=1
        dy=[0,0,1,-1]
        for f in range(4):
            fX= x+dx[f]
            fY= y+dy[f]
            if 0<=fX<7 and 0<=fY<8 and used[fY][fX]==False:
                if sorted([Nlist[y][x], Nlist[fY][fX]]) not in ST:
                    cnt+=1
                    return

    dx=[1,0]
    dy=[0,1]
    for i in range(2):
        X = x + dx[i]
        Y = y + dy[i]
        if 0<=X<7 and 0<=Y<8 and used[Y][X]==False:             #사용하지 않은 옆칸이면서 사용했던 짝이 아닌경우
            if sorted([Nlist[y][x], Nlist[Y][X]]) in ST:
                continue
            used[y][x],used[Y][X] = True,True
            ST.append(sorted([Nlist[y][x],Nlist[Y][X]]))

            s=0
            for u1 in range(8):                                 #사용안한 칸에서 다시 재귀
                for u2 in range(7):
                    if used[u1][u2] == False:
                        domino(u2,u1)
                        s=1
                        break
                if s==1:
                    break

            ST.pop()                                             #다시 되돌려놓기
            used[y][x], used[Y][X] = False, False




Nlist=[]
for _ in range(8):
    Nlist.append(input())
used=[[False]*7 for _ in range(8)]
ST=[]
cnt=0
domino(0,0)
print(cnt)