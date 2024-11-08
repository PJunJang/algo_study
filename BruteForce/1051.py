def square_size(a, b, board):
    size = 1 # size는 최소 1x1
    max_possible_edge = min(len(board[a])-b, len(board) - a)
    for i in range(1, max_possible_edge):
        # 네 꼭지점이 같은지 확인
        if (board[a][b] == board[a+i][b] and board[a][b] == board[a][b+i] and 
            board[a][b] == board[a+i][b+i]):
            size = (i+1) **2
    return size


N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())

# size = 1
size = 1 # init size to 1 since the min square is 1
for i in range(N):
    for j in range(M):
        # 각 점에서 사이즈를 재고 max로 계속 update
        size = max(size,square_size(i,j, board))
print(size)
