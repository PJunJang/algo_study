import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

Ts = [0] # 각 상담에 걸리는 시간
Ps = [0] # 각 상담당 수당

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    Ts.append(t)
    Ps.append(p)



# dp[n] = n 까지 가능한 최대 수익
dp = [0] * (N+1)
dp[0] = 0

for i in range(1,N+1):
    # print(f"i = {i}")
    # print(f"    Before :    dp[{i}] = {dp[i]}")
    # print(f"    Before :    dp[{i-1}] = {dp[i-1]}")
    # 이전날 수익으로 초기화
    dp[i] = max(dp[i], dp[i-1])
    # print(f"    after init: dp[{i}] = {dp[i]}")
    # print(f"    Ts[{i}]: {Ts[i]}, Ps[{i}]: {Ps[i]}")
    if i + Ts[i] - 1 <= N:
        # print(f"    before: dp[{i + Ts[i] - 1}]: {dp[i + Ts[i] - 1]}")
        dp[i + Ts[i] - 1] = max(dp[i + Ts[i] - 1], dp[i-1] + Ps[i])
        # print(f"    after:  dp[{i + Ts[i] - 1}]: {dp[i + Ts[i] - 1]}")
print(dp[N])


