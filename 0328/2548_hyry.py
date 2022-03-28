
# 일단은 모든 경우의 수를 구하자
# 그리고 arr list보다는 set으로 하는 것이 좋을 것 같다
# 그리고 sort도 필요하다

N = int(input())  # 자연수 개수
arr = list(map(int, input().split()))
numSet = sorted(set(arr))

minNum, minSum = 0, 1e10
for num in numSet:
    sumV = 0
    for i in arr:
        sumV += abs(num - i)
        if sumV > minSum:
            break
    if minSum > sumV:
        minSum = sumV
        minNum = num
    if sumV == 0:
        break

print(minNum)

# 방법 2 ㅠㅠ 😭
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
mid = n//2 - 1 if n % 2 == 0 else n//2
print(nums[mid])
