N = 4
directions = [0, [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
board = []

for i in range(N):
    board_row = []
    splt = input().strip().split()
    for j in range(N):
        board_row.append([int(splt.pop(0)), int(splt.pop(0))])
    board.append(board_row)

fish = {}
for x in range(N):
    for y in range(N):
        num = board[x][y][0]
        fish[num] = [[x, y], board[x][y][1]]

# print(board)
# print(fish)

board[0][0][0] = "S"
fish["S"] = [[0, 0], board[0][0][1]]

def print_board():
    for row in board:
        line = ""
        for f in row:
            line += str(f[0]) +" "
        print(line)
    print("")

def move_fish():
    global fish

    for fish_num in range(1, 17):
        x, y = fish[fish_num][0]
        orig_direction = board[x][y][1] 
        if board[x][y][0] == fish_num : # EXIST (NOT DEAD)
            while True:
                dx, dy = directions[board[x][y][1]]
                nx = x+dx; ny= y+dy
                if 0<=nx<N and 0<=ny<N:
                    if board[nx][ny][0] != "S":
                        board[nx][ny], board[x][y] = board[x][y], board[nx][ny]

                        fish[fish_num] = [(nx, ny), board[nx][ny][1]]
                        fish[board[x][y][0]] = [(x,y), board[x][y][1]]

                        # print("\nFISH-NUM {} <-> {}".format(fish_num, (nx, ny)))
                        break
                
                board[x][y][1] = (board[x][y][1] + 1) % 8 
                board[x][y][1] = board[x][y][1] if board[x][y][1] > 0 else 8

                if board[x][y][1] == orig_direction:
                    break

def DFS(cnt=0):
    global board
    # print("AFTER SHARK MOVE", fish)
    # print_board()

    move_fish()

    x, y = fish["S"][0]
    d = fish["S"][1]
    dx,dy = directions[d]

    # print("AFTER MOVE-FISH")
    # print_board()

    candidates = []
    for i in range(1, 4):
        nx = x+dx*i; ny=y+dy*i
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny][0] == 0:
                continue
            candidates.append((nx, ny))

    print("CAND", x, y, dx, dy, candidates)
    # for _ in board:
    #     print(_)
    # print("\n")

    if len(candidates) == 0 :
        return cnt

    # if (3, 3) in candidates:
    #     print("CAND", candidates)
    #     for _ in board:
    #         print(_)
    #     print("\n")

    max_v = 0; v= 0
    for cand in candidates:
        dead_x, dead_y = cand

        # print("PREV")
        # print(board)

        # print_board()
        print("CAND->", cand, candidates)        
        for _ in board:
            print(_)
        print("\n")

        prev_board = [row for row in board]

        ## 상태 바꾸기
        dead = board[dead_x][dead_y]
        board[dead_x][dead_y] = ["S", dead[1]]
        board[x][y] = [0, 0]

        prev_fish = fish["S"]
        fish["S"] = [[dead_x, dead_y], dead[1]]

        ## DFS
        v = DFS(cnt+dead[0])
        max_v = max(max_v, v)

        ## PREV로 돌리기
        fish["S"] = prev_fish
        fish[dead[0]] = [[dead_x, dead_y], dead[1]]
        board = prev_board

        print("CAND->", cand, candidates)        
        for _ in board:
            print(_)
        print("\n")

    
    return max_v




# move_fish()
v = DFS(0)
print(v)
