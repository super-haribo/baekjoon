N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
instructions = list(map(int, input().split()))

dice = {'top': 0, 'bottom': 0, 'front': 0, 'back': 0, 'left': 0, 'right':0}

def turn_1(dice):
    dice['top'], dice['right'], dice['bottom'], dice['left'] = dice['left'], dice['top'], dice['right'], dice['bottom']
    return dice

def turn_2(dice):
    dice['top'], dice['left'], dice['bottom'], dice['right']= dice['right'], dice['top'], dice['left'], dice['bottom']
    return dice

def turn_3(dice):
    dice['top'], dice['back'], dice['bottom'], dice['front'] = dice['front'], dice['top'], dice['back'], dice['bottom']
    return dice

def turn_4(dice):
    dice['front'], dice['top'], dice['back'], dice['bottom'] = dice['top'], dice['back'], dice['bottom'], dice['front']
    return dice

directions = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]

if board[x][y] == 0 :
    board[x][y] = dice['bottom']
else:
    dice['bottom'] = board[x][y]
    board[x][y] = 0

tops = []
for instr in instructions:
    dx, dy = directions[instr]
    nx = x+dx; ny=y+dy

    if 0>nx or 0>ny or nx>=N or ny>=M:
        continue

    x, y = nx, ny

    if instr == 1:
        dice = turn_1(dice)
    elif instr == 2:
        dice = turn_2(dice)
    elif instr == 3:
        dice = turn_3(dice)
    else:
        dice = turn_4(dice)

    if board[x][y] == 0 :
        board[x][y] = dice['bottom']
    else:
        dice['bottom'] = board[x][y]
        board[x][y] = 0

    tops.append(dice['top'])

for t in tops:
    print(t)




# dice ={'top': 1, 'bottom': 6, 'front': 5, 'back': 2, 'left': 4, 'right':3}
# print(dice)
# print(turn_1(dice))
