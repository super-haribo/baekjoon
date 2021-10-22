from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 각 칸에서 각 바이러스로 가는 시간 구해서 min 구하기
# 바이러스 후보 정해서 각 상태일 때, 최소 구하기

def virus_candidates():
    global board
    candidates = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                candidates.append((i, j))
    return candidates

def perms(N, M):
    # select M from N differnt numbers:
    result = [[] for _ in range(M)]
    result[0] = [[i] for i in range(N)]
    for i in range(1, M):
        for j in range(N):
            for r in result[i-1]:
                if (j not in r) and (r[-1] < j):
                    result[i].append(r + [j])

    return result[-1]

def isZeroInBoard(arr):
    for row in arr:
        if row.count(0) > 0:
            return True
    return False

def print_board(board):
    for row in board:
        print(row)
    print("\n")

candidates = virus_candidates()
virus_cand_num = len(candidates)
virus_cand_perm = perms(virus_cand_num, M)

dxdys = [(-1, 0), (1, 0), (0, 1), (0, -1)]

zero_num = 0
for row in board:
    zero_num += row.count(0)

min_time = N*N+N
for perm in virus_cand_perm: # FOR EACH CONDITION

    # initialize 
    # new_board = [[ 1 if (r ==1 or r == 2) else 0 for r in row] for row in board]
    new_board = [[r for r in row] for row in board]
    visited = [[0 for r in row] for row in board]

    virus = []
    for p in perm:
        x, y = candidates[p]
        new_board[x][y] = "*"
        virus.append((x, y))

        visited[x][y] = 1

    # spread virus
    time = 0; zero_count = 0
    # while len(virus) > 0:
    while zero_count < zero_num and len(virus) > 0 :
        time += 1
        spread = []
        for x, y in virus:
            for dx, dy in dxdys:
                nx = x+dx; ny = y+dy

                if 0<=nx<N and 0<=ny<N:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1

                        if new_board[nx][ny] != 1:
                            if new_board[nx][ny] == 0:
                                zero_count += 1
                            new_board[nx][ny] = 2
                            spread.append((nx, ny))


        # if zero_count == zero_num:
        #     break

        virus = spread

    # CANNOT SPREAD VIRUS PERFECTLY
    # isFinished = True
    # for row in new_board:
    #     if 0 in row:
    #         isFinished =False
    #         break
    isFinished = zero_count == zero_num

    if not isFinished:
        continue

    min_time = min(min_time, time)

if min_time != N*N+N:
    print(min_time)
else:
    print(-1)




'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
=> 4 (0,0) / 
'''
