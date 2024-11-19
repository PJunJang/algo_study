import sys
sys.setrecursionlimit(10**7)
# sys.stdin = open('input_11724.txt','r')


def DFS(graph, node, visited):
    visited[node] = True
    # print(node, end = " ")
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(graph, neighbor, visited)

from collections import deque
def BFS(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        # print(node, end = " ")
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


N, M = map(int, sys.stdin.readline().split())
# graph 노드는 1부터 N까지 있다. ==> 인접 리스트
graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)


visited = [False] * len(graph)
# for loop으로 graph의 모든 노드를 돌면서 연결되어있는 노드
cnt = 0
for node in range(1, N+1):
    if not visited[node]:
        BFS(graph, node, visited)
        cnt += 1
        # print(f"cnt: {cnt}")
print(cnt)
