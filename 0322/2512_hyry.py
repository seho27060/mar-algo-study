import sys
input = sys.stdin.readline

def bs(lst):

    # 가장 예산 높은 값과 예산의 합 구하기
    sumB = maxB = 0
    for money in lst:
        sumB += money
        if maxB < money:
            maxB = money

    # 예산의 합이 총 예산 내라면 그냥 리턴
    if sumB <= M: return maxB

    # 예산의 합이 총 예산보다 큰 경우

    start = 1
    end = maxB
    while start <= end:
        mid = (start + end) // 2
        budget = 0
        for money in lst:
            if money <= mid:
                budget += money
            else:
                budget += mid

        if budget == M: return mid
        elif budget < M:
            start = mid + 1
        else:
            end = mid - 1

    # 나온 값이 예산을 넘으면 mid - 1
    # 아니면 그대로 mid
    if budget > M: return mid - 1
    else: return mid


N = int(input())
R = list(map(int, input().split()))
M = int(input())
print(bs(R))

