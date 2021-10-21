N, M = map(int, input().split())
robot_x, robot_y, robot_d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
left_directions =[(0, -1), (-1, 0), (0, 1), (1, 0)]

def print_board():
    print("------ BOARD ------")
    for row in board:
        print(" ".join(map(str, row)))
    print("------ BOARD ------")


def SEARCH(robot_x, robot_y, robot_d, cnt):
    # print(robot_x, robot_y, robot_d)
    # print_board(); input()

    if board[robot_x][robot_y] == 0 :
        cnt += 1

    board[robot_x][robot_y] = 2

    for i in range(0, 4):
        new_d = (robot_d - i + 4) % 4
        dx, dy = left_directions[new_d]

        new_x = robot_x + dx
        new_y = robot_y + dy

        if 0<=new_x<N and 0<=new_y<M:
            if board[new_x][new_y] == 0 :
                return SEARCH(new_x, new_y, (robot_d - (i+1) + 4) % 4, cnt)

    new_x = robot_x + directions[robot_d][0]*(-1)
    new_y = robot_y + directions[robot_d][1]*(-1)

    if 0<=new_x<N and 0<=new_y<M:
        if board[new_x][new_y] != 1:
            return SEARCH(new_x, new_y, robot_d, cnt)

    return cnt

print(SEARCH(robot_x, robot_y, robot_d, 0))

'''
    0
3       1
    2
'''