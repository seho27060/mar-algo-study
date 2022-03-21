N, K = map(int, input().split())
A = list(map(int, input().split()))
V = [False] * N

def exercise(weight, n):
    if weight < 500 :
        return

    if n == N:
        global cnt
        cnt += 1
        return

    for i in range(N):
        if not V[i]:
            V[i] = True
            exercise(weight+A[i]-K, n+1)
            V[i] = False
cnt = 0
exercise(500, 0)
print(cnt)