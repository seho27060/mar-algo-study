n, k = map(int, input().split())
m = []
rank = []
for _ in range(n):
    m.append(list(map(int, input().split())))
m.sort(key=lambda x:(-x[1], -x[2], -x[3]))
r = 1
rank.append([m[0][0], r])
cnt = 0
for i in range(1, n):
    r += 1
    r += cnt
    if m[i][1:4] == m[i-1][1:4]:
        cnt += 1
        r -= cnt
        rank.append([m[i][0], r])
    else:
        cnt = 0
        rank.append([m[i][0], r])
rank.sort()
print(rank[k-1][1])