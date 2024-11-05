

def find_two(lis):
    total_sum = sum(lis)
    first, second = 0, 0
    if(lis):
        for i in range(9):
            first = lis[i]
            for j in range(i+1, len(lis)):
                second = lis[j]
                if (total_sum - (first + second) == 100):
                    return [first, second]
    return None
    

heights = []
for _ in range(9):
    heights.append(int(input()))

two_fakes = find_two(heights)
if two_fakes:
  heights.remove(two_fakes[0])
  heights.remove(two_fakes[1])
  heights.sort()
  for h in heights:
    print(h)






    
