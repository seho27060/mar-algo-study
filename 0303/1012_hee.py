N = int(input())

arr = list(map(int, input().split()))
max_val = -1
ans = []
for i in range(N,-1,-1):
    if i > max_val :
