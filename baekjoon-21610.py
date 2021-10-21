N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
instrs = [list(map(int, input().split())) for _ in range(M)]
directions = [0, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0 ,1], [1, 1], [1, 0], [1, -1]]
diags = [[1, -1], [-1, 1], [1, 1], [-1, -1]]

def print_board():
    for r in board:
        print(r)
    print("\n")

def move_cloud(clouds, di, si): # step1
    global N
    new_cloud = []
    dx = directions[di][0] * si
    dy = directions[di][1] * si

    for i in range(len(clouds)):
        cx, cy = clouds[i]
        nx = (cx+dx+N*si)%N
        ny = (cy+dy+N*si)%N
        # new_cloud.append((nx, ny))
        
        clouds[i] = (nx, ny)
        # print("(dx,dy)=({}, {}), (cx, cy)=({}, {}) => {}, {}".format(dx, dy, cx, cy, nx, ny))
        # print(cy, dy, N*si, (cy+dx+N*si)%N); input()

    # return new_cloud

def add_rain_1(clouds): # step2
    global board
    for cx, cy in clouds:
        board[cx][cy] += 1

def add_rain_diag(clouds): # step4
    for cx, cy in clouds:
        cnt = 0
        for dx, dy in diags:
            nx = cx+dx; ny= cy+dy
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] >= 1:
                    cnt += 1

        board[cx][cy] += cnt

def make_cloud(clouds):
    new_clouds = []
    for x in range(N):
        for y in range(N):
            if (board[x][y] >= 2):
                if ((x,y) not in clouds):
                    board[x][y] -= 2
                    new_clouds.append((x,y))
    return new_clouds

def total_step():
    clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

    for di, si, in instrs:
        print("------------({}, {}) --------------".format(di, si))
        

        # clouds = move_cloud(clouds, di, si)
        move_cloud(clouds, di, si)
        print("CLOUDS", clouds)##

        add_rain_1(clouds)
        # print_board() ## 

        add_rain_diag(clouds)
        # print_board() ## 

        clouds = make_cloud(clouds)
        print("CLOUDS", clouds)##

        # print("\n", di, si)
        print_board(); input()
    
    water = 0
    for row in board:
        water += sum(row)

    return water

print(total_step())

'''
5 4
0 0 1 0 2
2 3 2 1 0
4 3 2 9 0
1 0 2 9 0
8 8 2 1 0
1 3
3 4
8 1
4 8
'''