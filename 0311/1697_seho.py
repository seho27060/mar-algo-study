import sys
sys.setrecursionlimit(100000)
def bfs(get_,count):
    global m,answer,visited
    ## count 번째 이동에 m이 포함되어 있다면, 재귀 중지.
    if m in get_:
        answer = count
        return
    else:
        queue = []
        ## 탐색 후보들 순회
        for tmp in get_:
            ## 해당 탐색 후보에서 -1, +1, *2의 이동으로 탐색.
            for i in [-1,1,tmp]:
                ## 조건에 부합 하나면, 다음 탐색 후보로 추가.
                if tmp + i not in visited and 0<= tmp + i <=100000:
                    visited.add(tmp+i)
                    queue.append(tmp+i)
    ## 탐색 후보가 있다면, bfs 재귀적 시행.
    if queue:
        bfs(queue,count+1)
## 이미 다녀갔다면, 굳이 갈필요가 없다, 이미 최소거리를 넘어갔으니,
## bfs로 구현.

n,m = map(int,input().split())
visited = set()
answer = 0
bfs([n],0)
print(answer)