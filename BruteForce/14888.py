from itertools import permutations

# ('+', '-', '*', '/')
def calculate(numbers, ops):
    res = numbers[0]
    for i in range(1, len(numbers)):
        if ops[i-1] == "+":
            res += numbers[i]
        elif ops[i-1] == "-":
            res -= numbers[i]
        elif ops[i-1] == "*":
            res *= numbers[i]
        elif ops[i-1] == "/":
            # 나눗셈은 음수 양수 case:
            if res > 0:
                res = res // numbers[i]
            else:
                tmp = res*(-1)
                res = (tmp // numbers[i]) * (-1)
    return res





# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))
ops_count = list(map(int, input().split()))  # +, -, *, / 의 개수

# 연산자 리스트 생성
operators = []  # 빈 리스트 생성
operators.extend(['+'] * ops_count[0])
operators.extend(['-'] * ops_count[1])
operators.extend(['*'] * ops_count[2])
operators.extend(['/'] * ops_count[3])

# 가능한 연산자 순열 생성
op_permutations = set(permutations(operators))
# print(op_permutations)

max_res = -100000000000
min_res = 100000000000

for ops in op_permutations:
    res = calculate(numbers, ops)
    max_res = max(max_res, res)
    min_res = min(min_res, res)
    
print(max_res)
print(min_res)
