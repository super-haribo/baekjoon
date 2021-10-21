N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dxdys = [(1, 0), (-1, 0), (0, 1), (0, -1)]
score = 0

def print_board():
    # VISUALIZING BOARD
    global board
    for row in board:
        line = ""
        for r in row:
            line += str(r).rjust(2) +" "
        print(line)
    print("\n")

def gravitiy():
    global board
    for i in range(N-1, -1, -1): # START AT BOTTOM
        for j in range(N):
            if board[i][j] != "X": # ONLY START AT EMTPY BOARD
                continue
                
            highest = i
            while highest >= 0 and board[highest][j] == "X":
                if board[highest-1][j] == -1:
                    highest = i
                    break
                elif board[highest-1][j] == "X":
                    highest -= 1

                elif board[highest-1][j] >= 0 :
                    highest -= 1
                    break

            if highest < 0 :
                highest = 0
            
            if highest != i:
                board[highest][j], board[i][j] = board[i][j], board[highest][j] 

def rotate():
    global board
    new_board = []
    for col_idx in range(N-1, -1, -1):
        col = []
        for i in range(N):
            col.append(board[i][col_idx])
        new_board.append(col)
    board = new_board

def autoplay():
    global board, N, M, score

    while True:
        ################################
        # STEP 1 (FIND GROUP)s
        visited = [[0 for i in range(N)] for _ in range(N)]
        group_candidates = [] # (block_num , rainbow_num, row_len, col_len)
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1 or board[i][j] == 0:
                    continue

                # PASS IF EMPTY / BLACK / RAINBOW
                if board[i][j] in ["X", -1]:
                    visited[i][j] = 1
                    continue

                # GROUPING
                stack = [(i, j)]
                color = board[i][j]
                visited[i][j] = 1
                group = {"color": [(i, j)], 'rainbow': []}
                while len(stack) > 0 :
                    x, y = stack.pop()
                    for dx, dy in dxdys:
                        nx = x+dx; ny = y+dy
                        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                            c = board[nx][ny]
                            if c == "X" or c == -1: # EMPTY or BLACK
                                visited[nx][ny] = 1
                                continue
                            if c == 0 or c == color: 
                                if c==0: # RAINBOW
                                    if (nx, ny) in group['rainbow']:
                                        continue
                                    group['rainbow'].append((nx, ny))
                                else:   # SAME COLOR BLOCK
                                    visited[nx][ny] = 1
                                    group['color'].append((nx, ny))

                                stack.append((nx, ny))

                block_num = len(group['rainbow']) +  len(group['color'])
                if block_num < 2: # IF A BLOCK GROUP DOESN'T HAVE 2 OR MORE BLOCKS 
                    continue
                
                # GET STANDARD BLOCK (X, Y)
                group['color'].sort(key=lambda x: (x[0], x[1]))
                std_row, std_col = group['color'][0]

                # group_info -> (block_num , rainbow_num, row_len, col_len)
                group_info = [block_num, len(group['rainbow']), std_row, std_col, group['color'], group['rainbow']]
                group_candidates.append(group_info)
        
        ## END CONDITION
        if len(group_candidates) == 0:
            break

        # SELECT BIGGEST BLOCK-GROUP
        group_candidates.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
        selected_group = group_candidates[0]
        b = selected_group[0]; score += pow(b, 2)

        # REMOVE BLOCK-GROUP
        for x, y in selected_group[4]:
            board[x][y] = "X"

        for x, y in selected_group[5]:
            board[x][y] = "X"

        ########################
        # print("REMOVE BLOCK, SCORE +=", pow(b, 2))
        # print_board()

        gravitiy()
        # print("GRAVITY")
        # print_board()

        rotate()
        # print("ROTATE")
        # print_board()

        gravitiy()
        # print("GRAVITY")
        # print_board()

        # print_board()
        # input()
        # print(board); input()

# print(" ")
# print_board()
autoplay()
print(score)

'''
INPUT EXAMPLE

4 3
1 1 1 3
3 2 3 3
1 2 -1 3
-1 -1 1 1
=> 33

6 4
2 3 1 0 -1 2
2 -1 4 1 3 3
3 0 4 2 2 1
-1 4 -1 2 3 4
3 -1 4 2 0 3
1 2 2 2 2 1
=> 125

5 3
0 0 0 0 1
-1 -1 0 -1 0
-1 -1 3 -1 -1
-1 -1 0 -1 -1
0 0 2 0 0
=> 74
'''
