from itertools import permutations

def weight():
    global cnt
    plus = 0
    for i in range(n):
        plus += a[c[i]]
        plus -= k
        if plus < 0:
            return
    cnt += 1
    return

n, k = map(int, input().split())
a = list(map(int, input().split()))
com = list(permutations(list(range(n)), n))
cnt = 0
for c in com:
    weight()
print(cnt)