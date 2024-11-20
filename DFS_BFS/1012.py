import sys
sys.setrecursionlimit(10**7)
# sys.stdin = open('input_1012.txt','r')


def DFS(graph, node, visited):
    visited[node] = True
    # print(node, end = " ")
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(graph, neighbor, visited)

def dfs(grid, i, j, visited):
    visited[i][j] = True
    directions = [(-1,0), (1,0), (0,-1) , (0,1)]
    for dx, dy in directions:
        nx , ny = i + dx, j + dy
        # valid range 안에서 탐색
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == True:
            dfs(grid, nx, ny, visited)

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

def bfs(graph, start, visited):
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


# N, M = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[False]*M for _ in range(N)] # grid N x M으로 init
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        grid[y][x] = True
        
    visited = [[False] * M for _ in range(N)]
    # 연결 component의 개수가 바로 필요한 배추흰지렁이 수다.
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == True and not visited[i][j]:
                dfs(grid, i, j, visited)
                cnt += 1
    print(cnt)
