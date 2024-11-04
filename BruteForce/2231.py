def digit_sum(n):
    res = 0
    for i in str(n):
        res += int(i)
    res += n
    return res


N = int(input())
# res to store the ans
res = 0
for i in range(0, N):
    if digit_sum(i) == N:
        res = i
        break

if res != 0:
    print(res)
else:
    print(0)



