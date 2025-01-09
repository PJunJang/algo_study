def solution(nums):
    answer = 0
    
#     1.set으로 중복 제거하여 전체 가지수를 알 수 있다.
#     2. 만약 nums에 dup이 없다면, len(nums)//2 가 최대 types이다.

    uniques = set(nums)
    unique_types = len(uniques)
    max_types = len(nums) // 2
    answer = min(unique_types, max_types)

    return answer
