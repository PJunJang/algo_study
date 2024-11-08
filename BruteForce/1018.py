def cnt_repaints(board, first_color, x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[x + i][y + j] != first_color:
                    cnt += 1
            else: # 만약 홀수 칸이라면,
                if board[x+i][y+j] == first_color:
                    cnt += 1
    return cnt



N , M = map(int, input().split())
# print(N,M)

# first get current board with input
board = []
for i in range(N):
    board.append(input())

# now cut board in 8x8 size from anywher and cnt
cnt = 1000000000000
for i in range(N-7):
    for j in range(M-7):
        w_cnt = cnt_repaints(board, 'W', i, j)
        b_cnt = cnt_repaints(board, 'B', i, j)
        
        cnt = min(cnt, w_cnt, b_cnt)
print(cnt)
