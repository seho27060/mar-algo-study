
import sys
input = sys.stdin.readline


def topdown(lst, downward=True):
    new_lst = lst[::]
    # downward=True 위에서 내려가기
    # downward=False 아래에서 위로 올라가기
    for row in range(rNum) if downward else range(rNum - 1, -1, -1):
        for col in range(len(ladder[0])):
            if ladder[row][col] == '?':
                return new_lst
            if ladder[row][col] == '-':
                new_lst[col], new_lst[col + 1] = new_lst[col + 1], new_lst[col]


def buildLadder(new_s, new_g):
    result = ''
    for idx in range(pNum - 1):
        if new_s[idx] == new_g[idx]:
            result += '*'
        elif new_s[idx] == new_g[idx + 1] and new_g[idx] == new_s[idx + 1]:
            result += '-'
            new_s[idx], new_s[idx + 1] = new_s[idx + 1], new_s[idx]
        else:
            result = 'x' * (pNum - 1)
            break

    return result

    # idx = 0
    # while idx < pNum:
    #     if new_s[idx] == new_g[idx]:
    #         result += '*'
    #         idx += 1
    #     else:
    #  오류난 부분..? 왜일까...
    #         if idx <= pNum - 2 and new_s[idx] == new_g[idx + 1] and new_g[idx] == new_s[idx + 1]:
    #             result += '-' if idx == pNum - 2 else '-*'
    #             idx += 2
    #         else:
    #             result = 'x' * (pNum - 1)
    #             return result




pNum = int(input().rstrip())  # 참가한 사람 수
rNum = int(input().rstrip())   # 전체 행 수
goal = list(input().rstrip())  # 끝지점
start = sorted(goal)  # 시작지점
ladder = [list(input().rstrip()) for _ in range(rNum)]

new_s = topdown(start)
new_g = topdown(goal, downward=False)
print(buildLadder(new_s, new_g))
