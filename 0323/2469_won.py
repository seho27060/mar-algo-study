k = int(input())
n = int(input())
p = input().strip()
first = [i for i in range(27)]
first = first[:k]
first = list(map(lambda i: chr(ord('A') + i), first))
ladder = [input().strip() for _ in range(n)]
for i in range(n):
    for j in range(k - 1):
        if ladder[i][j] == '-':
            first[j], first[j + 1] = first[j + 1], first[j]
        elif ladder[i][j] == '?':
            break
    if ladder[i] == '?' * (k - 1):
        break
# print(first)

p = list(p)
for i in range(n - 1, -1, -1):
    for j in range(k - 1):
        if ladder[i][j] == '-':
            p[j], p[j + 1] = p[j + 1], p[j]
        elif ladder[i][j] == '?':
            break
    if ladder[i] == '?' * (k - 1):
        break
# print(p)

i = 0
sol = ''
while i < k - 1:
    if first[i] == p[i] and first[i + 1] == p[i + 1]:
        sol += '*'
    else:
        if first[i] == p[i + 1] and first[i + 1] == p[i]:
            sol += '-'
        else:
            sol += '*'
    i += 1
# print(sol)

for i in range(k - 1):
    if sol[i] == '-':
        first[i], first[i + 1] = first[i + 1], first[i]

if ''.join(first) == ''.join(p):
    print(sol)
else:
    print('x' * (k - 1))
