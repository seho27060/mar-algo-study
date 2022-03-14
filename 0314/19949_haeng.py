Nlist = list(map(int, input().split()))
cnt = 0
omr=[]

def test(x):
    global cnt
    if 6<=x<=9:                                   #5점이 넘지않는경우 미리 컷
        point = 0
        for j in range(x):
            if Nlist[j] == omr[j]:
                point += 1
        if point == x-6:
            return

    if x == 10:
        for k in range(0,8):                       # 연속된 3자리 컷
            if omr[k]==omr[k+1]==omr[k+2]:
                return

        point=0
        for j in range(10):                        # 5점이상인경우 카운트
            if Nlist[j] == omr[j]:
                point += 1
        if point >= 5:
            cnt += 1
        return

    for i in range(1,6):                           #리턴되기 전까지 append
        omr.append(i)                              #리턴받으면 pop후 포문계속
        test(x+1)
        omr.pop()


test(0)
print(cnt)