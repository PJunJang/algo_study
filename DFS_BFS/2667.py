import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input_2667.txt','r')


def dfs(grid, i, j, visited):
    visited[i][j] = True
    dirs = [(-1,0), (1,0), (0,-1) , (0,1)]
    danji_cnt = 1
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if 0 <= nx < len(visited) and 0 <= ny < len(visited[i]) and not visited[nx][ny] and grid[nx][ny] == "1":
            danji_cnt += dfs(grid, nx, ny, visited)
    return danji_cnt

grid = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    row = sys.stdin.readline()
    grid.append(row)

visited = [[False]*N for _ in range(N)]

cnt = 0 # 연결 component의 개수를 센다
danji_lis = []
# danji_cnt = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == "1" and not visited[i][j]:
            
            danji_cnt = dfs(grid, i, j, visited)
            danji_lis.append(danji_cnt)
            cnt += 1
print(cnt)
danji_lis.sort()
for d in danji_lis:
    print(d)

