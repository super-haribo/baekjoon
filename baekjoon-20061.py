########################################################################
# TREAT GREEN AND BLUE AREA EQUALLY AFTER ADDED BLOCK
# WHEN ADDING A BLOCK, ADDED POSITION CHANGED FOR BLUE AREA
#         AND THE BLOCK WILL PLACE ON THE 2ND ROW 

# 초록 영역과 파란 영역에 블록이 추가 된 이후의 처리는 동일하게 진행
# 블록이 각 영역에 추가될 때, 두번째 row (idx==1)에 포함되도록 추가되며
#           파란색 영역에 추가될 때에는 x, y가 서로 바뀌어 추가된다 
#                   e.g. (2, 1) -> (1, 1) / (1, 3) -> (3, 2)
########################################################################

green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(4)] for _ in range(6)]
score = 0

def print_status(status): # HELPER FUNCTION
    for row in status:
        print(row)
    print("\n")

def add_green(t, x, y):
    global green
    if t == 1:
        green[1][y] = 1
    elif t == 2:
        green[1][y] = 1
        green[1][y+1] = 1
    elif t == 3:
        green[0][y] = 1
        green[1][y] = 1

def add_blue(t, x, y):
    global blue
    if t == 1:
        blue[1][3-x] = 1
    elif t == 2:
        blue[0][3-x] = 1
        blue[1][3-x] = 1
    elif t == 3:
        blue[1][3-x] = 1
        blue[1][3-x-1] = 1

def how_much_go_down(status):
    # HOW MUCH DOSE THE ADDED BLOCK NEED TO GO DOWN?
    # 2ND ROW TO WHERE? 

    downs = []
    for idx in range(4):
        if status[1][idx] == 1:
            if status[2][idx] == 1:
                downs.append(0)
                continue

            next_row = 1
            while next_row+1 < 6 and status[next_row+1][idx] != 1:
                next_row += 1

            downs.append(next_row - 1)

    return min(downs)


def pushdown(status):
    global score 

    # PUSH DOWN
    down_cnt = how_much_go_down(status)
    row0 = [i for i in status[0]]
    row1 = [i for i in status[1]]

    status[0]=[0 for _ in range(4)]
    status[1]=[0 for _ in range(4)]

    row_idx = 1; move_idx = down_cnt+row_idx
    status[move_idx] = [x+y for x, y in zip(status[move_idx], row1)]
    row_idx = 0; move_idx = down_cnt+row_idx
    status[move_idx] = [x+y for x, y in zip(status[move_idx], row0)]

    # REMOVE FULL ROW
    row_idx = 2
    while row_idx < len(status):
        if sum(status[row_idx]) == 4:
            status.pop(row_idx)
            score += 1 #### 1 SCORE UP
        else:
            row_idx += 1

    # REMOVE REMAIN ROW
    if sum(status[0]) > 0:
        # PUSH DOWN 2 ROWS
        status = status[:4]

    elif sum(status[1]) > 0:
        # PUSH DOWN 1 ROW
        status = status[:5]

    # PAD TO MAKE 6*4 
    row_num = len(status)
    if row_num != 6:
        status =[[0 for _ in range(4)] for _ in range(6-row_num)] + status

    return status


N = int(input())
instructions = [list(map(int, input().split())) for _ in range(N)]
for instr in instructions:
    t, x, y = instr
    add_green(t, x, y)
    add_blue(t, x, y)

    green = pushdown(green)
    blue = pushdown(blue)

cnt = 0
for row in green:
    cnt += sum(row)
for row in blue:
    cnt += sum(row)

print(score)
print(cnt)
