N = int(input())
num_apples = int(input())
apples = [input().split() for _ in range(num_apples)]
num_turns = int(input())
turns = [input().split() for _ in range(num_turns)]; turns = [[int(t1), t2] for t1, t2 in turns]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right bottom left top



board = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(apples)):
    a_x, a_y = apples[i]
    a_x = int(a_x) - 1
    a_y = int(a_y) - 1
    board[a_x][a_y] = 'A'
    apples[i] = [a_x, a_y]

def print_board():
    for row in board:
        print(row)
    print("\n")

from collections import deque

time = 1
x, y, d = [0, 0, 0]
snakes = deque(); snakes.append((0, 0)); board[0][0] = 1

while True:
    dx, dy = directions[d]
    nx = x+dx; ny = y+dy

    if 0>nx or nx>=N or 0>ny or ny>=N:
        break
    
    if board[nx][ny] == 1 :
        break

    if board[nx][ny] == 0:
        assert board[nx][ny] == 0

        t_x, t_y= snakes.popleft() #tail
        board[t_x][t_y] = 0

    snakes.append((nx, ny))
    board[nx][ny] = 1

    ## if time end, turn 
    if len(turns) > 0:
        if time == turns[0][0]:
            _, turn = turns.pop(0)

            if turn == "L":
                d = (d-1+4) % 4
            else :
                d = (d+1) % 4

    time += 1
    x, y = nx, ny

print(time)