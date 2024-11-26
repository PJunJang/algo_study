import sys

# 파일에서 입력을 읽어오는 부분
sys.stdin = open('input_1463.txt', 'r')

# 입력 받기
n = int(sys.stdin.readline())

# 1. DP 테이블 초기화
dp = [1000000] * (n+1)
# print(dp)
dp[1] = 0 # 1에서 1을 만들때는 연산 수가 0
# print(f"dp[1] = {dp[1]}")

for i in range(2, n+1):
    print(f"\n현재 i = {i}을(를) 처리합니다.")
    # 1 을 빼는 경우
    dp[i] = dp[i-1] + 1
    print(f"    1을 빼는 경우: dp[{i-1}] + 1 = {dp[i-1]} + 1 = {dp[i]}")
    # 2로 나눠지면 2로 나눈다
    if i % 2 == 0:
        print(f"    {i} % 2 == 0:")
        tmp = dp[i//2] + 1
        # print(f"    dp[{i}//2] + 1 = {tmp}")
        print(f"    dp[{i}] = {dp[i]} and tmp = {tmp}")
        dp[i] = min(dp[i], tmp)
        print(f"    dp[{i}] = {dp[i]}")
    if i % 3 == 0:
        print(f"    {i} % 3 == 0:")
        tmp = dp[i//3] + 1
        print(f"    dp[{i}//3] + 1 = {tmp}")
        print(f"    dp[{i}] = {dp[i]} and tmp = {tmp}")
        dp[i] = min(dp[i], tmp)
        print(f"    dp[{i}] = {dp[i]}")
    
    print(f"dp[{i}] = {dp[i]}")
print(dp[n])




