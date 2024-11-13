
def get_index(board, num):
    for i in range(5):
        if num in board[i]:
            return (i,board[i].index(num))

# take checked_idx and return if it's three bingo
def is_bingo(checked_idx):
    # print(checked_idx)
    cnt = 0
    
    # row and column에서 몇개의 axis가 체크되었는지 cnt위한 list
    row_cnt = [0]*5
    col_cnt = [0]*5
    diag_1 = 0
    diag_2 = 0
    diag_1_lis = [(i,i) for i in range(5)]
    diag_2_lis = [(i,4-i) for i in range(5)]
    
    for x,y in checked_idx:
        row_cnt[x] += 1
        col_cnt[y] += 1
        if (x,y) in diag_1_lis:
            diag_1 += 1
        if (x,y) in diag_2_lis:
            diag_2 += 1
    
    cnt += row_cnt.count(5)
    cnt += col_cnt.count(5)
    if diag_1 == 5: 
        cnt += 1
    if diag_2 == 5:
        cnt += 1
    return cnt >= 3
    

def bingo(board, mc):
    bingo_cnt = 0
    checked_idx = []
    
    for i in range(len(mc)):
        # print(f"index of {mc[i]} : {get_index(board, mc[i])}")
        checked_idx.append(get_index(board, mc[i]))
        if(is_bingo(checked_idx)):
            print(i+1)
            return
    
    


# first take board
board = []
for _ in range(5):
    line = list(map(int, input().split()))
    # print(line)
    board.append(line)
# print("Board:")
# print(board)

# then take 사회자 call
mc = []
for _ in range(5):
    line = list(map(int, input().split()))
    for num in line:
        mc.append(num)


bingo(board, mc)
# print("mc:")
# print(mc)

# get bingo
