import sys

sys.stdin = open('input_2748.txt','r')

n = int(sys.stdin.readline())

memo = {}

def fibo_dp_top_down(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]
    
    memo[n] = fibo_dp_top_down(n-1) + fibo_dp_top_down(n-2)
    return memo[n]

print(fibo_dp_top_down(n))
