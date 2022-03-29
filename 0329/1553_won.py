arr = [list(map(int, input())) for _ in range(8)]
# print(arr)

v = [[False] * 7 for _ in range(8)]
cnt = 0

domi = []
for i in range(7):
    for j in range(i, 7):
        domi.append([i, j])
# print(domi)

def f():
    global cnt
    for si in range(8):
        for sj in range(7):
            if v[si][sj] == False:
                r(si, sj)
                return
        if not domi:
            cnt += 1
            return

def r(si, sj):
    for di, dj in [[0, 1], [1, 0]]:
        ni, nj = si + di, sj + dj
        if 0 <= ni < 8 and 0 <= nj < 7 and v[ni][nj] == False and ([arr[si][sj], arr[ni][nj]] in domi or [arr[ni][nj], arr[si][sj]] in domi):
            p = 0
            for k in range(len(domi)):
                if domi[k] == [arr[si][sj], arr[ni][nj]] or domi[k] == [arr[ni][nj], arr[si][sj]]:
                    p = k
                    break
            tmp = domi.pop(p)
            v[si][sj] = v[ni][nj] = True
            f()
            domi.append(tmp)
            v[si][sj] = v[ni][nj] = False
r(0, 0)
print(cnt)