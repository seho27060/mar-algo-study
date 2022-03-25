import sys
input = sys.stdin.readline

N = int(input())
C = int(input())
students = list(map(int, input().split()))

pictures = []
votes = []
inList = [False] * 101  # 학생 번호에 기반
pCnt = 0

for s in students:

    # 이미 들어있다면
    if inList[s]:
        votes[pictures.index(s)] += 1
    else: # 들어있지 않을 때
        if pCnt < N:  # 액자가 다 안 찬 경우
            pictures.append(s)
            votes.append(1)
            inList[s] = True
            pCnt += 1
        else:
            # 액자가 다 찬 경우인데 새로 추가해야 하는 경우
            # 1. minV 체크 그리고 이 minV가 얼마 등장하는지 체크
            minV = 1e10
            for idx in range(N):
                if minV > votes[idx]:
                    minV = votes[idx]
                    pIdx = idx
                    cnt = 1
                elif minV == votes[idx]:
                    cnt += 1
            if cnt == 1:
                # 가장 적게 추천받은 학생이 한 명인 경우
                t = pictures.pop(pIdx)
                votes.pop(pIdx)
                inList[t] = False
                pictures.append(s)
                votes.append(1)
                inList[s] = True
            else:
                t = pictures.pop(pIdx)
                votes.pop(pIdx)
                inList[t] = False
                pictures.append(s)
                votes.append(1)
                inList[s] = True

pictures.sort()
print(*pictures)