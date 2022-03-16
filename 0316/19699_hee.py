from itertools import combinations
import math

N, M = map(int, input().split())
cows = list(map(int, input().split()))
max_sum = sum(cows)

prime = [1] * (max_sum + 1)
prime[1] = 0
chk = 2
ans = set() # 중복 방지

def prime_func(x): # 에라토스테네스의 체
    temp = int(math.sqrt(x))
    for j in range(2, temp+1):
        if prime[j] == 1:
            for k in range(j*j, max_sum + 1, j):
                prime[k] = 0

for i in combinations(cows, M):
    s = sum(i)
    prime_func(s)
    if prime[s] == 1:
        ans.add(s)

ans = list(ans)
if ans :
    ans.sort()
    print(*ans)
else:
    print(-1)