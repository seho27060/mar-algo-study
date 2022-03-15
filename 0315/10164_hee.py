N, M, K = map(int, input().split())
def paths(r, c, init):
    arr = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                arr[j][i] = init
            else:
                arr[j][i] = arr[j-1][i] + arr[j][i-1]
    return arr[-1][-1]
if K == 0:
    ans = paths(N, M, 1)
else:
    x, y = (K - 1) % M, (K - 1) // M
    val = paths((x+1), (y+1), 1)
    ans = paths((M-x), (N-y), val)
print(ans)