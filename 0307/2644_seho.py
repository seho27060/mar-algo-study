def bfs(start_,end_):
    global visited,lst
    ## 다음 너비 탐색 후보를 위한 빈 리스트
    queue = []      ## ==> set으로 구현해도 될지도?..

    ## for 문으로 dqque에서의 FIFO 구조를 구현 가능
    ## 탐색할 노드 순회
    for i in start_:
        ## 탐색 노드의 인접 노드 순회
        for j in lst[i-1]:
            ## 해당 노드를 방문하지 않았다면,
            if visited[j-1] == -1:
                ## 탐색을 시작한 노드 i의 길이 값 + 1을 대입
                visited[j-1] = visited[i-1] + 1
                ## 노드가 도착지라면 return, 재귀 종료
                if j == end_:
                    return
                ## 다음 탐색 후보에 j 대입
                queue.append(j)

    ## 다음에 탐색할 후보 노드가 있다면,
    ## 해당 노드 리스트에 대한 재귀적 bfs 실행
    if queue:
        bfs(queue,end_)

## 부모자식? 방향?
## 최단거리, 부모 노드 - 자식 노드 => (트리 or 그래프)
## ==>> bfs 풀이.
n = int(input())
## 출발점, 목적지
start_, end_ = map(int,input().split())
## 인접리스트 구현을 위한 빈 리스트
lst = [[] for _ in range(n)]
## 방문 배열/ -1로 초기화
visited = [-1]*n

m = int(input())

for i in range(m):
    ## 부모자식 이라고 해서 방향이 있나?.. 라고 생각했으나,
    ## 동갑내기 사촌을 찾아갈려면 부모자식 노드의 관계는 양방향이여야 한다.
    a,b = map(int,input().split())
    lst[a-1].append(b)
    lst[b-1].append(a)
    ## 양방향 인접리스트 생성

## 너비 탐색에 있어서 임의적인 오름차순 탐색을 위해 정렬.
lst = list(map(sorted,lst))

## 시작점의 방문 배열 0 으로 초기화.
visited[start_-1] = 0

## bfs 시작
bfs([start_],end_)
print(visited[end_-1])
