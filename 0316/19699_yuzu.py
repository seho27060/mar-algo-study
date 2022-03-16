from itertools import combinations
n, m = map(int, input().split())
com = []
for i in combinations(list(range(n)), m):
    com.append(list(i))
h = list(map(int, input().split()))
h.sort()

prime = []
for c in com:
    num = 0
    while c:
        num += h[c[-1]]
        c.pop()
    prime.append(num)

max = 0
for j in range(n, n-m, -1):
    max += h[j-1]
arr = [0, 0] + [1]*(max-1)
ans = []
for k in range(2, max+1):
    if arr[k] == 1:
        if k in prime:
            ans.append(k)
        for l in range(2*k, max+1, k):
            arr[l] = 0

print(*ans) if ans else print(-1)