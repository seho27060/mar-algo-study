
def permu(depth, N):

    if depth >= 2:
        if signs[depth - 2] == '>' and numbers[depth - 2] < numbers[depth - 1]: return
        elif signs[depth - 2] == '<' and numbers[depth - 2] > numbers[depth - 1]: return

    if depth == N:
        nums = ''
        for i in numbers:
            nums += str(i)
        result.append(nums)
        return

    for num in range(10):
        if not used[num]:
            numbers[depth] = num
            used[num] = True
            permu(depth + 1, N)
            used[num] = False



K = int(input())
signs = input().split()

numbers = [-1] * (K + 1)
used = [False] * 10
result = []

permu(0, K + 1)

minV = '9999999999'
maxV = '0'
for i in result:
    if maxV < i:
        maxV = i
    if minV > i:
        minV = i
print(maxV)
print(minV)