from collections import deque

def findmysister(N, K):
    # Q = []
    Q = deque()
    visited = [0] * 100_001

    if N == K:
        return 0

    Q.append(N)
    visited[N] += 1

    while Q:
        currPos = Q.popleft()
        if currPos == K:
            return visited[K] - 1
        for dp in (2, 1, -1):
            if dp == 2:
                newPos = currPos * dp
            else:
                newPos = currPos + dp

            if 0 <= newPos <= 100_000 and visited[newPos] == 0:
                Q.append(newPos)
                visited[newPos] = visited[currPos] + 1

    return visited[K] - 1


N, K = map(int, input().split())
print(findmysister(N, K))