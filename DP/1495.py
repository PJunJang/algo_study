import sys
sys.stdin = open('input.txt','r')

# N: 곡 갯수, S: 시작 볼륨, M: max constraint
N, S, M = map(int, sys.stdin.readline().split())

# 변경 가능 볼륨 리스트
V = [0]
V.extend(list(map(int, sys.stdin.readline().split())))


# 각 index에다 가능한 볼륨을 리스트로 append해준다
dp = [[] for _ in range(N+1) ]
dp[0].append(S)
# print(f"init dp:    {dp}")

for i in range(1, N+1):
    possible_volumes = set()
    for volume in dp[i-1]:  # 이전 곡에서 가능한 볼륨 순회
        if volume + V[i] <= M:
            # print(f"volume: {volume} ; dp[{i}-1]: {dp[i-1]}")
            possible_volumes.add(volume + V[i])
            # print(f"    at {i}, possible_volumes = {possible_volumes}")
        if volume - V[i] >= 0:
            possible_volumes.add(volume - V[i])
            # print(f"    at {i}, possible_volumes = {possible_volumes}")
    dp[i] = (list(possible_volumes))
    # print(f"dp[{i}] : {dp[i]}")
if dp[N]:
    print(max(dp[N]))
else:
    print(-1)

# print(N,S,M)
