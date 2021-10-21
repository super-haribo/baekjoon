N, M, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)] #  ri, ci, mi, si, di

board = [[[] for _ in range(N)] for _ in range(N)]
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

# INITIALIZE
for ball in infos:
    r, c, m, s, d = ball
    r -= 1; c-= 1
    board[r][c] = [(m, s, d)]

# CHECK ALL DIRECTIONS ARE EVEN OR ODD
def all_even_or_odd(ds):
    all_even = True
    all_odd = True
    for d in ds:
        if d % 2 == 0:
            all_odd = False
        else:
            all_even = False
    return all_odd or all_even

for _ in range(K):
    # FOR EACH TRIAL
    new_board= [[[] for _ in range(N)] for _ in range(N)]

    # MOVE FIRE BALL
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) > 0:
                for ball in board[x][y]:
                    m, s, d = ball 
                    dx, dy = directions[d]

                    nx = (x+dx*s+N)%N ; ny=(y+dy*s+N)%N # MOVE
                    assert 0<=nx<N and 0<=ny<N 
                    new_board[nx][ny].append((m, s, d))

    # IF SOME FIREBALLS MEET TOGETHER, DIVIDE THOSE 
    for x in range(N):
        for y in range(N):
            balls = new_board[x][y]
            if len(balls) <= 1: # 1 FIREBALL IN THIS POSITION
                board[x][y]= new_board[x][y]
                continue

            # DIVIDE FIRE BALL
            board[x][y] = []
            m_s = []; s_s = []; d_s = []
            for m, s, d in balls:
                m_s.append(m)
                s_s.append(s)
                d_s.append(d)
            
            new_m = int(sum(m_s) // 5)
            if new_m == 0: # IF MASS IS EQUAL TO 0, PASS
                board[x][y] = []
                continue
            new_s = int(sum(s_s) // len(s_s))
            new_d = [0, 2, 4, 6] if all_even_or_odd(d_s) else [1, 3, 5, 7]
            for d in new_d:
                board[x][y].append((new_m, new_s, d))

# CHECK FINAL TOTAL MASS
total_m = 0
for x in range(N):
    for y in range(N):
        for ball in board[x][y]:
            m, s, d= ball
            total_m += m

print(total_m)
