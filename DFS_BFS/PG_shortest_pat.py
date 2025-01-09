from collections import deque


def bfs(maps, start, target):
    n, m = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((start[0], start[1], 1))
    # print(queue)
    visited[start[0]][start[1]] = True
    # print(visited)
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x,y) == target:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny,dist+1))
    return -1
    
    
    
    
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    return bfs(maps, (0,0), (n-1,m-1))
    
