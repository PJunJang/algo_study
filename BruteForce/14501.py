# 입력 받기
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# DP 테이블 초기화
dp = [0] * (N + 1)

# DP 계산
for i in range(N):
    # 현재까지의 최대 이익을 다음 날에 전달
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]
    else:
        dp[i + 1] = dp[i + 1]
    # 상담이 기간 내에 끝나는지 확인
    if i + T[i] <= N:
        if dp[i + T[i]] < dp[i] + P[i]:
            dp[i + T[i]] = dp[i] + P[i]
        else:
            dp[i + T[i]] = dp[i + T[i]]

# 최대 이익 출력
print(dp[N])
