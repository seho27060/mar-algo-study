N = int(input())
A = list(map(int, input().split()))

def calcul(A):  # 절댓값 계산
    result = 0
    for i in range(N - 1):
        result += abs(A[i] - A[i + 1])
    return result

def max_val(A, idx):  # 자리 교환
    global ans
    ans = max(calcul(A), ans)

    if idx == N - 1:
        return
    for i in range(idx + 1, N):
        A[idx], A[i] = A[i], A[idx]
        max_val(A, idx + 1)
        A[idx], A[i] = A[i], A[idx]


ans = -10 ** 9
max_val(A, 0)
print(ans)