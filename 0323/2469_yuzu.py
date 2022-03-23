def ladder():
    for i in range(n):
        for j in range(k - 1):
            if arr[i][j] == '-':
                start[j], start[j + 1] = start[j + 1], start[j]
            elif arr[i][j] == '?':
                return start

def ladder_rev():
    for i in range(n-1, -1, -1):
        for j in range(k - 1):
            if arr[i][j] == '-':
                end[j], end[j + 1] = end[j + 1], end[j]
            elif arr[i][j] == '?':
                return end

k = int(input())
n = int(input())
end = list(input())
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
start = alphabet[:k]
arr = [list(input()) for _ in range(n)]

s = ladder()
e = ladder_rev()

ans = ''
for i in range(k - 1):
    if s[i] == e[i]:
        ans += '*'
    elif s[i] == e[i+1] and s[i+1] == e[i]:
        ans += '-'
        s[i], s[i+1] = s[i+1], s[i]
    else:
        ans = 'x' * (k - 1)
        break
print(ans)