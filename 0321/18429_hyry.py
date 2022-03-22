from itertools import permutations

N, K = map(int, input().split())  # k = 매일 매일 근 손실량
A = list(map(int, input().split()))

cnt = 0
for plan in permutations(A, N):
    muscle = 500
    for d in plan:
        muscle += d
        muscle -= K
        if muscle < 500:
            break
    else:
        cnt += 1

print(cnt)


# ----------------------------
def plan(depth, muscle):
    global cnt
    if muscle < 500: return
    if depth == N: cnt += 1; return

    for idx in range(N):
        if not used[idx]:
            used[idx] = True
            plan(depth + 1, muscle + A[idx] - K)
            used[idx] = False

    return cnt


N, K = map(int, input().split())  
A = list(map(int, input().split()))
used = [False] * N
cnt = 0
print(plan(0, 500))