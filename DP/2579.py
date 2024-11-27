import sys

sys.stdin = open('input_2579.txt', 'r')

n = int(sys.stdin.readline())
stairs = [0]
for _ in range(1, n+1):
    tmp = int(sys.stdin.readline())
    stairs.append(tmp)
    
if n == 1:
    print(stairs[1])
    sys.exit()
if n == 2:
    print(stairs[1]+ stairs[2])
    sys.exit()
# print(f"stairs: {stairs}")
# dp [i] 정의: i번째까지 최대점수
# dp[] init:
dp = [0] * (n+1)
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

# dp 점화식
# 1. 한번에 한 계단(두계단 + 한계단): 
#   dp[i] = dp[i-3] + stairs[i-1] + stairs[i]
# 2. 한번에 두 계단: 
#   dp[i] = dp[i-2] + stairs[i]

for i in range(3, n+1):
    print(f"cur i = {i}")
    # 1번 케이스
    dp[i] = dp[i-3] + stairs[i-1] + stairs[i]
    print(f"    1번케이스: dp[{i}] = {dp[i]}")

    # 2번 케이스
    tmp = dp[i-2] + stairs[i]
    print(f"    2번케이스: dp[{i}] = {tmp}")

    # 최종 dp[i] => max
    dp[i] = max(dp[i], tmp)
    print(f"    최종 dp[{i}] = {dp[i]}")

print(dp[n])

    

# print(dp)
