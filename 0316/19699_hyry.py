

def isPrime(num):
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True


def cooow(N, depth):

    if depth > 0:
        onecnt = zerocnt = 0
        for idx in range(depth):
            if bits[idx]:
                onecnt += 1
            else:
                zerocnt += 1
            if onecnt > M: return
            if zerocnt > N - M: return

    if N == depth:
        if bits.count(1) == M:
            s_cows.append(bits[::])
            # 2차원이라 참조하는 게 같아서 지금 같이 바뀌어버림 ㅎㅎ
        return

    for i in (0, 1):
        if not selected[depth]:
            bits[depth] = i
            selected[depth] = True
            cooow(N, depth + 1)
            selected[depth] = False


N, M = map(int, input().split())
cows = list(map(int, input().split()))

bits = [-1] * N
selected = [False] * N
s_cows = []

cooow(N, 0)

result = set()
for bit in s_cows:
    sumV = 0
    for cIdx in range(N):
        if bit[cIdx]:
            sumV += cows[cIdx]
    if isPrime(sumV):
        result.add(sumV)

if len(result) == 0:
    print(-1)
else:
    result = sorted(result)
    print(*result)

