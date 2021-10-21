N, M  = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxdys = [(1, 0), (-1, 0), (0, -1), (0, 1)]

walls= []
def count_vacteria(chk_board):    
    board = [[r for r in row] for row in chk_board]
    
    wall=""
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'A':
                wall +="({},{})".format(i, j)
    walls.append(wall)


    for i in range(N):
        for j in range(M):
            if board[i][j] != 2:
                continue

            stacks=[(i, j)]
            while len(stacks) > 0:
                x, y = stacks.pop()
            
                for dx, dy in dxdys:
                    nx = x+dx; ny = y+dy
                    if 0<=nx<N and 0<=ny<M:
                        if board[nx][ny] != 1:
                            board[nx][ny] = 2
                            stacks.append((nx, ny))
    cnt = 0
    for row in board:
        cnt += row.count(0)

    return cnt


def build_wall(board, wall_cnt, R, C):
    if wall_cnt == 3:
        cnt = count_vacteria(board)
        return cnt


    max_cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 'A'
                cnt = build_wall(board, wall_cnt + 1, i, j)
                max_cnt = max(max_cnt, cnt)
                board[i][j] = -1
    
    return max_cnt

print(build_wall(board, 0, 0, 0))
print(len(walls), len(set(walls)))