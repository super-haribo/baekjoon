top= (1, 0); bottom = (-1, 0)
left= (0, -1); right= (0, 1) 

cctv1 = [[top], [bottom], [left], [right]]
cctv2 = [[top, bottom], [left, right]]
cctv3 = [[top, right], [right, bottom], [bottom, left], [left, top] ]
cctv4 = [[top, right, bottom], [top, bottom, left], [top, right, left], [right, bottom, left]]
cctv5 = [[top, right, bottom, left]]

direction_cctvs = [0, cctv1, cctv2, cctv3, cctv4, cctv5]
n_cctv =[0, 4, 2, 4, 4, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

board_cctvs = []
for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 6:
            board_cctvs.append((board[i][j], i, j))

def print_board():
    for row in board:
        print(" ".join([str(r) for r in row]))
    print("\n")

def search(cctv_idx, arr):
    global board

    if cctv_idx >= len(board_cctvs):
        cnt = 0
        for row in board:
            cnt += row.count(0)
        return cnt


    cctv, x, y = board_cctvs[cctv_idx]
    directions = direction_cctvs[cctv]

    board_copy = [[r for r in row] for row in board]

    min_v = N*M
    for i in range(len(directions)):
        direction = directions[i]
        board = [[r for r in row] for row in board_copy]

        for d in direction:
            dx, dy = d; nx, ny = x, y
            while True:
                nx += dx
                ny += dy

                if nx<0 or ny<0 or nx>=N or ny>=M:
                    break

                if board[nx][ny] == 6:
                    break
                else:
                    board[nx][ny] = "#"

        v = search(cctv_idx+1, arr+[i])
        min_v = min(min_v, v)

    return min_v

print(search(0, []))