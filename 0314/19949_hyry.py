
import sys
input = sys.stdin.readline

def jjikki(N, depth):
    global cnt, answer_sheet, answer
    # if correct >= 5:
    #     cnt += 1
    #     correct = 0
    #     return
    # if incorrect >= 6:
    #     incorrect = 0
    #     return
    if depth >= 5:
        correct = incorrect = 0
        for idx in range(depth):
            if answer_sheet[idx] == answer[idx]:
                correct += 1
            else:
                incorrect += 1
        if depth == N and correct >= 5:
            cnt += 1
            return
            # return
        elif incorrect >= 6:
            return

    # if N == depth:
    #     return

    for num in range(1, 5 + 1):
        if depth > 1 and answer_sheet[depth - 2] == answer_sheet[depth - 1] == num:
            continue

        answer_sheet[depth] = num
        jjikki(N, depth + 1)


answer = list(map(int, input().split()))

cnt = 0
answer_sheet = [0] * 10
jjikki(10, 0)

print(cnt)






# if N == depth:
#     # print(answer_sheet)
#     # if answer[depth - 1] == answer_sheet[depth - 1]:
#     #     correct -= 1
#     # else:
#     #     incorrect -= 1
#     # print(correct, incorrect)
#     return
# if N == depth:   # 테스트용
#     print(answer_sheet)
#     return