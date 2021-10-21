N = int(input())
favorites = [list(map(int, input().split())) for _ in range(pow(N, 2))]
order = [row[0] for row in favorites]; favorites = {k[0]:set(k[1:]) for k in favorites}
board = [[0 for _ in range(N)] for _ in range(N)]
dxdys = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
#2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
#3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

def find_index(num):
    global board
    lst = []
    favorite = favorites[num]
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                ngh = 0; fav = 0 #neighbors/favorites
                for dx, dy in dxdys:
                    nx = x+dx; ny=y+dy
                    if 0<=nx<N and 0<=ny<N:
                        v = board[nx][ny]
                        if v == 0:
                            ngh += 1
                        if v in favorite:
                            fav += 1
                lst.append([fav, ngh, x, y])
    lst.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # if num == 9:
    #     print(lst)

    x, y = lst[0][2:]
    return [x, y]

def print_board():
    global board
    for r in board:
        print(r)
    print("\n")

for num in order:
    x, y = find_index(num)
    board[x][y] = num

    # print("\n", num)
    # print_board()

answer = 0
score_dict = {0 : 0, 1: 1, 2: 10, 3:100, 4:1000}
for x in range(N):
    for y in range(N):
        num = board[x][y]
        # score = len(adjacent[x][y].intersection(favorites[num]))
        #  0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
        score = 0
        for dx, dy in dxdys:
            nx = x+dx; ny=y+dy
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] in favorites[num]:
                    score += 1

        answer += score_dict[score]
print(answer)

'''
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4
->
9	3	2
8	4	7
5	6	1
-> 54
'''
