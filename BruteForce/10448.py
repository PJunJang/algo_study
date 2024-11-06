def getallTs(n):
    Tns = set()
    for i in range(1, n+1):
        Ti = i*(i+1)//2
        # print(f"T{i} = {Ti}")
        Tns.add(Ti)
    return Tns

# takes Tns as an arg to check whether it's ans or not
def isAns(s, n):
    res = 0
    for first in s:
        for second in s:
            third = n - first - second
            if (third in s):
                return True
    return False

# print(isAns([1,4,6]))
  
# the number of input on top
n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

for i in nums:
    if(isAns(getallTs(i), i)):
        print(1)
    else:
        print(0)
    
