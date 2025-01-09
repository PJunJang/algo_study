def solution(participant, completion):
    answer = ''
    part_dict = {}
    
#     dictionary 채워주기
    for p in participant:
        if p in part_dict:
            part_dict[p] += 1
        else:
            part_dict[p] = 1
            
#     completion 돌면서 part_dict value 업데이트해주기
    for c in completion:
        if c in part_dict:
            part_dict[c] -= 1
    
#     정답 업데이트
    for k,v in part_dict.items():
        # print(k)
        if part_dict[k] == 1:
            return k
    
    return answer
