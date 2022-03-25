N = int(input())
M = int(input())
arr = list(map(int, input().split()))

A = [] # 사진틀 / 앞에 있는 사진일수록 게시된지 오래된 사진
B = [] # 추천 수
for i in arr:
    for j in range(len(A)): # 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우, 추천받은 횟수만 증가
        if A[j] == i:
            B[j] += 1
            break
    else:
        if len(A) < N: # 사진틀이 비어있는 경우 사진 올리기
            A.append(i)
            B.append(1)
            continue
        else: # 사진틀이 비어있지 않은 경우, 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고 추가
            idx = B.index(min(B))
            A.pop(idx)
            B.pop(idx)
            A.append(i)
            B.append(1)
A.sort()
print(*A)
