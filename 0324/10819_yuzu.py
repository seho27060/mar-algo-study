from itertools import permutations

def maxv(p):
    sum = 0
    for i in range(n-1):
        sum += abs(a[p[i]]-a[p[i+1]])
    return sum

n = int(input())
a = list(map(int, input().split()))
ans = 0
for p in permutations(range(n)):
    res = maxv(p)
    if res>ans:
        ans = res
print(ans)