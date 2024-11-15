from itertools import combinations

# print(board)
# 풀이 디자인:
# 1. 가능한 팀 조합을 itertools로 combination (members, N// 2)
#     - 나머지는 전부 다른팀
# 2. 능력치 계산: 팀별 합

# 3. 모든 조합을 iterate하면서 min 비교


def cal_ability(team, board):
    ability = 0
    for i in team:
        for j in team:
            ability += board[i][j]
    return ability


board = []
N = int(input())
for i in range(N):
    board.append(list(map(int, input().split())))

members = []
for i in range(N):
    members.append(i)
        
# print(members)

min_diff = 1000000

for team in combinations(members, N//2):
    team1 = set(team)
    team2 = set(members) - team1 # 상대편
    
    ability1 = cal_ability(team1, board)
    ability2 = cal_ability(team2, board)

    # 절댓값
    diff = abs(ability1 - ability2)
    min_diff = min(min_diff, diff)
    
print(min_diff)
    
    


