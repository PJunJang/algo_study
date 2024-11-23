import sys
# sys.stdin = open('input_12851.txt','r')
sys.stdin = open('input_1697.txt','r')

from collections import deque


N, K = map(int, sys.stdin.readline().split())

def bfs(start, target):
    visited = [-1] * 100001
    time = 0  # level 탐색 (queue 레벨 넘어갈때만 +1)
    min_time, count = -1, 0     # 최단 거리, 최단거리 경로 수
    cur_pos = start  

    queue = deque()
    queue.append((cur_pos, time))
    visited[cur_pos] = time
    
    while queue:
        cur_pos, time = queue.popleft()
        # print(f"current pos: {cur_pos} and current time: {time}")
        if cur_pos == target:
            if min_time == -1: # 처음 찾은 경우
                min_time = time
                count = 1
            elif time == min_time:
                count += 1
            continue
        
        
        for next_pos in [cur_pos-1, cur_pos+1, cur_pos*2]:
            if  0 <= next_pos < len(visited):
                # print(f"next pos: {next_pos}")
                if visited[next_pos] == -1:  # 처음 방문 케이스
                    visited[next_pos] = time + 1
                    queue.append((next_pos, time + 1))
                elif visited[next_pos] == time + 1:    
                    # 이미 방문 했지만 최소 시간으로 갈 수 있는 경우 
                    queue.append((next_pos, time + 1))

                # print(f"current queue: {queue}")
                # print(f"current visited: {visited}")
    return min_time, count


# 최소 시간과 경로 수 출력
min_time, count = bfs(N, K)
print(min_time)
print(count)
