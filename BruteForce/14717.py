from itertools import combinations

def get_score(card1, card2):
    if card1 == card2:
        return 10 + card1
    else:
        return (card1 + card2) % 10

def get_probability(a, b):
    # 모든 카드 목록
    cards = []
    for i in range(1,11):
        cards.append(i)
        cards.append(i)
    # 내 핸즈 제외
    cards.remove(a)
    cards.remove(b)
    
    # 내 핸즈 score 계산
    my_score = get_score(a, b)
    
    # 상대 가능 패 조합
    possible_ops_hands = list(combinations(cards,2))
    total_cases = len(possible_ops_hands)
    cnt = 0
    
    for op in possible_ops_hands:
        op_score = get_score(op[0], op[1])
        if my_score > op_score:
            cnt += 1
    
    # 승률 계산
    res = cnt / total_cases
    return (f"{res:.3f}")
    
    
    
    
a, b = map(int, input().split())
print(get_probability(a,b))
