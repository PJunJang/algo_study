import sys
sys.setrecursionlimit(10**7)
from collections import deque

sys.stdin = open('input_1697.txt','r')


# 이 문제는 최단시간을 구해야 하므로 bfs로 푸는것이 좋겠다.
def bfs(start, target):

    visited = [False] * 100001
    queue = deque()
    queue.append((start, 0))   # (start, time)
    visited[start] = True
    # print(f"current start: {start}")
    

    while queue:
        cur_pos, time = queue.popleft()
        # print(f"current pos: {cur_pos}")
        if cur_pos == target:
            return time
        for next_pos in [cur_pos-1, cur_pos+1, cur_pos*2]:
            if 0 <= next_pos <= len(visited) and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))
                # print(f"current queue: {queue}")
                # print(f"current visited: {visited}")
        






# take input: N, K
N, K = map(int, sys.stdin.readline().split())
print(bfs(N, K))
