#브루트포스

import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
V = [False] * N
L = N

if sum(lst) <= M: # 모든 요청이 배정될 수 있는 경우
    print(max(lst))

else: # 배정할 수 없는 경우, 특정한 정수 상한액 계산
    budget = 0
    while True:
        if M - N >= 0: # 예산 분배
            budget += 1
            M -= N
        else:
            break

        for i in range(L): # 요청한 금액을 충족한 경우 제외
            if not V[i] and budget >= lst[i]:
                V[i] = True
                N -= 1
    print(budget)