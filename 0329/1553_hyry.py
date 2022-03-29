import sys
from itertools import combinations_with_replacement as comb
input = sys.stdin.readline


def putDomino(row, col, cnt):  # 현재 row, col & 도미노 놓은 개수 cnt
    global tCnt

    if row == 8:  # board를 모두 순회했을 때
        if cnt == 28:  # 놓은 주사위 수가 28개라면
            tCnt += 1  # 경우의 수 + 1
        return

    if visited[row][col]:  # 새로운 좌표에 왔더니 이미 놓았던 곳이라면?
        if col + 1 != 7:  # 다음에 갈 col 좌표가 범위를 넘어서지 않는다면
            putDomino(row, col + 1, cnt)  # 놓은 도미노가 없으니 cnt는 그대로
        else:  # 다음에 갈 col 좌표가 범위를 넘어 선다면
            putDomino(row + 1, col - col, cnt)
            # col 좌표는 0으로 초기화, row는 하나 늘려준다

    # 새로운 좌표에 놓을 장소가 있다면?
    # 지금 row, col 좌표와 visited 여부는 체크 완료된 상황
    # newR, newC만 체크하면 된다
    else:
        for dr, dc in ((1, 0), (0, 1)):  # 아래, 오른쪽 방향
            newR = row + dr
            newC = col + dc

            if 0 <= newR < 8 and 0 <= newC < 7 and not visited[newR][newC]:
                # row, col가 도미노 왼쪽, newR, newC이 도미노 오른쪽
                if (board[row][col], board[newR][newC]) in dominos and \
                        (board[row][col], board[newR][newC]) not in used:
                    visited[row][col] = visited[newR][newC] = True
                    used.add((board[row][col], board[newR][newC]))
                    if col + 1 != 7:
                        putDomino(row, col + 1, cnt + 1)
                    else:
                        putDomino(row + 1, col - col, cnt + 1)
                    visited[row][col] = visited[newR][newC] = False
                    used.remove((board[row][col], board[newR][newC]))

                # newR, newC가 도미노 왼쪽, row, col이 도미노 오른쪽
                elif (board[newR][newC], board[row][col]) in dominos and\
                        (board[newR][newC], board[row][col]) not in used:
                    visited[row][col] = visited[newR][newC] = True
                    used.add((board[newR][newC], board[row][col]))
                    if col + 1 != 7:
                        putDomino(row, col + 1, cnt + 1)
                    else:
                        putDomino(row + 1, col - col, cnt + 1)
                    visited[row][col] = visited[newR][newC] = False
                    used.remove((board[newR][newC], board[row][col]))


dominos = set(comb((i for i in range(7)), 2))  # 도미노 셋 생성
used = set()  # 사용한 도미노
board = [list(map(int, list(input().rstrip()))) for _ in range(8)]
visited = [[False] * 7 for _ in range(8)]
tCnt = 0  # 가능한 경우의 수
putDomino(0, 0, 0)
print(tCnt)
