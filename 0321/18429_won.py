n, k = map(int, input().split())
kit = list(map(int, input().split()))

used = [False] * n
w = 500
def f(i, w):
    global cnt
    if w < 500:
        return
    if i == n:
        # print(arr)
        cnt += 1
        # flag = True
        # for j in arr:
        #     w += j - k
        #     if w < 500:
        #         flag = False
        # if flag:
        #     cnt += 1
        return
    for j in range(n):
        if not used[j]:
            used[j] = True
            f(i + 1, w + kit[j] - k)
            used[j] = False
cnt = 0
f(0, w)
print(cnt)
