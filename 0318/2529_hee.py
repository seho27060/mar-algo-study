k = int(input())
E = list(input().split())
E.reverse()
def calcul(A, arr):
    if not arr:
        global min_ans, max_ans, chk
        if not chk : # 첫 번째 : 최소값
            min_ans = list(lst)
            chk = True
            return
        else: # 마지막 : 최대값
            max_ans = list(lst)
            return

    B = arr.pop()
    if B == '<':
        for a in range(A+1,10):
            if not visited[a]:
                lst.append(a)
                visited[a] = True
                calcul(a, arr)
                visited[a] = False
                lst.pop()

    elif B == '>':
        for a in range(A):
            if not visited[a]:
                lst.append(a)
                visited[a] = True
                calcul(a, arr)
                visited[a] = False
                lst.pop()
    arr.append(B)

min_ans, chk = [], False
visited = [False] * 10
for i in range(10):
    lst = [i]
    visited[i] = True
    calcul(i, list(E))
    visited[i] = False

print(''.join(map(str, max_ans)))
print(''.join(map(str, min_ans)))
