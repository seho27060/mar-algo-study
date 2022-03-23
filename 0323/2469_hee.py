from string import ascii_uppercase
import sys

def ladder(t_idx, b_idx):
    start = b_idx
    if b_idx == (k-1):
        return ''.join(L[blank_line])
    # 위에서부터 내려오기
    for i in range(blank_line):
        if -1 < t_idx - 1 < k - 1 and L[i][t_idx-1] == '-':
            t_idx -= 1
        elif -1 < t_idx < k - 1 and L[i][t_idx] == '-':
            t_idx += 1
    # 아래서부터 올라가기
    for i in range(n-1, blank_line, -1):
        if -1 < b_idx - 1 < k - 1 and L[i][b_idx-1] == '-':
            b_idx -= 1
        elif -1 < b_idx < k - 1 and L[i][b_idx] == '-':
            b_idx += 1
    # 아래부터 올라갔을 때 위치 == 위에서 내려왔을 때 위치 : '*'
    if t_idx == b_idx:
        if (-1 < t_idx - 1 < k - 1 and L[blank_line][t_idx - 1] == '-') or (-1 < t_idx < k - 1 and L[blank_line][t_idx]) == '-':
            return 'x' * (k-1)
        else:
            if -1 < t_idx - 1 < k - 1:
                L[blank_line][t_idx - 1] = '*'
            if -1 < t_idx < k - 1:
                L[blank_line][t_idx] = '*'

    # 아래부터 올라갔을 때 위치 < 위에서 내려왔을 때 위치 : 둘 사이에 '-' ( 좌우는 '*'여야함 )
    elif t_idx > b_idx:
        if (-1 < t_idx - 1 < k - 1 and L[blank_line][t_idx-1] == '*') or not(-1 < t_idx - 1 < k - 1):
            return 'x' * (k-1)
        else:
            if -1 < t_idx - 2 < k - 1:
                L[blank_line][t_idx - 2] = '*'
            if -1 < t_idx - 1 < k - 1:
                L[blank_line][t_idx - 1] = '-'
            if -1 < t_idx < k - 1:
                L[blank_line][t_idx] = '*'

    # 아래부터 올라갔을 때 위치 > 위에서 내려왔을 때 위치 : 둘 사이에 '-' ( 좌우는 '*'여야함 )
    elif t_idx < b_idx:
        if (-1 < t_idx < k - 1 and L[blank_line][t_idx] == '*') or not(-1 < t_idx < k - 1):
            return 'x' * (k-1)
        else:
            if -1 < t_idx - 1 < k - 1 :
                L[blank_line][t_idx - 1] = '*'
            if -1 < t_idx < k - 1:
                L[blank_line][t_idx] = '-'
            if -1 < t_idx + 1 < k - 1 :
                L[blank_line][t_idx + 1] = '*'

    return ladder(dic[result[start+1]], start+1)

alphabet_list = list(ascii_uppercase)
dic = {}
for idx, i in enumerate(alphabet_list):
    dic[i] = idx

k = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
result = list(sys.stdin.readline().strip())

L = []
B = []
for i in range(n):
    line = list(sys.stdin.readline().strip())
    L.append(line)
    if line == ['?'] * (k-1):
        blank_line = i

print(ladder(dic[result[0]], 0))