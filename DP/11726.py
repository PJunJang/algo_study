import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())


# 2xn size rectangle을 1x2, 2x1 tile로 채우는 방법
# dp[n] => 2xn 을 채우는 방법 수

# 최종적으로 dp[n] % 10,007을 print

# init dp
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1
if n >= 2:
    dp[2] = 2
# print(dp)

# 점화식:
# 마지막에 오는 경우의 수 dp[n]만 생각하면된다
# 1. 2*1 세로 한개 => dp[n-1]
# 2. 1*2 가로로 두개 => dp[n-2]
# thus... dp[n] = dp[n-1] + dp[n-2]

# fill dp[]
if n >= 3:
    for i in range(3, n+1):
        # print(f"at {i}: ")
        dp[i] = dp[i-1] + dp[i-2]
        # print(dp[i])
print(dp[n]%10007)
