Domino = []
for i in range(7):
    for j in range(i, 7):
        Domino.append((i,j))
# 28개의 도미노

M = []
for _ in range(8):
    l = [int(i) for i in list(input())]
    M.append(l)

D = [(1,0), (0,1)]
# 도미노를 가로로 놓는 경우 / 세로로 놓는 경우

arr = [[-1] * 7 for _ in range(8)] # 방문여부
cnt = 0 # 경우의 수
def case(n):
    if n == 0: # 모든 도미노를 배치한 경우
        global cnt
        cnt += 1
        return

    flag = False
    for i in range(8):
        for j in range(7):
            if flag:
                break

            if arr[i][j] == -1:
                for d in D:
                    ni = i + d[1]
                    nj = j + d[0]
                    if -1 < nj < 7 and -1 < ni < 8 and arr[ni][nj] == -1:
                        if (M[i][j], M[ni][nj]) in Domino:
                            temp = Domino.pop(Domino.index((M[i][j], M[ni][nj])))
                            arr[i][j] = M[i][j]
                            arr[ni][nj] = M[ni][nj]
                            case(n-2)
                            arr[i][j] = -1
                            arr[ni][nj] = -1
                            Domino.append(temp)

                        if ((M[i][j], M[ni][nj]) not in Domino) and ((M[ni][nj], M[i][j]) in Domino):
                            temp = Domino.pop(Domino.index((M[ni][nj], M[i][j])))
                            arr[i][j] = M[i][j]
                            arr[ni][nj] = M[ni][nj]
                            case(n-2)
                            arr[i][j] = -1
                            arr[ni][nj] = -1
                            Domino.append(temp)
                flag = True

case(56)
print(cnt)