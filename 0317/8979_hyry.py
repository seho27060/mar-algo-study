import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medals = [(0, 0, 0, 0) for _ in range(N + 1)]

for _ in range(N):
    land, G, S, B = map(int, input().split())
    medals[land] = (G, S, B, land)

ranking = sorted(medals, key=lambda x: (x[0], x[1], x[2]), reverse=True)

rank = 0
for a, b, c, d in ranking:
    rank += 1
    if d == K: break
    elif (a, b, c) == (medals[K][0], medals[K][1], medals[K][2]):
        rank -= 1
print(rank)
