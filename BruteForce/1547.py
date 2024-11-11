

# input
M = int(input())

cups= [1,2,3]

for i in range(M):
    x, y = map(int, input().split())
    # x와 y의 위치를 swap
    idx_x = cups.index(x)
    idx_y = cups.index(y)
    
    cups[idx_x], cups[idx_y] = cups[idx_y], cups[idx_x]

print(cups[0])


# 아래는 더 효율적인 풀이법이다.
# # 초기 공의 위치는 1번 컵 아래
# ball = 1

# # 입력 받기
# M = int(input())
# for _ in range(M):
#     x, y = map(int, input().split())
#     # 공이 현재 x나 y에 위치한 경우 위치를 변경
#     if ball == x:
#         ball = y
#     elif ball == y:
#         ball = x
# print(ball)
