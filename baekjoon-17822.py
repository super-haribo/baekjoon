N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]; board = [[]] + board
instrs = [list(map(int, input().split())) for _ in range(T)] # xi, di, ki

def print_board(b): # HELPER FUNCTION
    for row in b:
        print(row)
    print("\n")

def getAverage():
    global board
    sum_v = 0; num_v = 0
    for row in board:
        for r in row:
            if r != "X":
                sum_v += r 
                num_v += 1

    return sum_v, num_v

for xi, di, ki in instrs:
    # TURN
    for i in range(1, N+1):
        if i * xi > N:
            break
        
        row_idx = i * xi; row = board[row_idx]
        if di == 0:
            new_row = row[-ki:] + row[:-ki]
        else:
            new_row = row[ki:] + row[:ki] 
        board[row_idx] = new_row

    # ERASE (SAME & ADJACENCY)
    Erased = False
    new_board = [[] for _ in range(N+1)]
    for r in range(1, N+1):
        for c in range(M):
            if board[r][c] == "X":
                new_board[r].append("X")
                continue

            left = (c-1+M)%M; right = (c+1+M)%M
            isInnerExist = r-1>0;  isOuterExist = r+1 <= N # IF ROW == 1 or ROW == N

            compare = [board[r][left], board[r][right]]
            if isInnerExist:
                compare.append(board[r-1][c])
            if isOuterExist:
                compare.append(board[r+1][c])

            # ERASE OR NOT
            if board[r][c] not in compare:
                new_board[r].append(board[r][c])
            else:
                new_board[r].append("X")
                Erased = True


    # IF NOTHING HAS BEEN ERASED
    if not Erased:
        sum_v, num_v = getAverage()
        if num_v == 0: # CATCH "DIVIDE BY ZERO" ERROR
            continue

        avg = sum_v / num_v
        for r in range(1, N+1):
            for c in range(M):
                v= new_board[r][c]
                if v=="X":
                    continue
                if v > avg:
                    new_board[r][c] -= 1
                elif v < avg:
                    new_board[r][c] += 1

    board = new_board

s, v = getAverage()
# SUMMATION
print(s)
