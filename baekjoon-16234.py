N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dxdys = [[-1, 0], [1, 0], [0, 1], [0, -1]]

from collections import deque

def DFS(cluster, cluster_num, x, y):
    if cluster[x][y] != 0:
        return cluster, cluster_num, 0, 0

    # stacks = [(x, y)]
    stacks = deque(); stacks.append((x, y))
    cluster[x][y] = -1
    cluster_added = 0
    total_sum = board[x][y]; total_num = 1

    # cluster_founded = []
    while len(stacks) > 0 :
        # x, y = stacks.pop()
        x, y = stacks.popleft()
        # cluster_founded.append((x, y))

        for dx, dy in dxdys:
            nx = x+dx
            ny = y+dy

            if 0<=nx<N and 0<=ny<N:
                if cluster[nx][ny] != 0 :
                    continue

                if L <= abs(board[nx][ny] - board[x][y]) <= R:
                    cluster[nx][ny] = cluster_num
                    cluster[x][y] = cluster_num

                    stacks.append((nx, ny))
                    cluster_added = 1 

                    total_sum += board[nx][ny]
                    total_num += 1


    if cluster_added == 0 :
        total_sum = 0
        total_num = 0
    else:
        # for x, y in cluster_founded:
        for x in range(N):
            for y in range(N):
                if cluster[x][y] == cluster_num:
                    board[x][y] = total_sum // total_num

    return cluster, cluster_num + cluster_added, total_sum, total_num

cnt = 0
while True:
    # cluster -> 0 not-visited / -1 visited / >= 1 cluster
    cluster = [[0 for _ in range(N)] for _ in range(N)]  
    cluster_num = 1
    # total = [0 for i in range(N*N//2)]; num = [0 for i in range(N*N//2)]

    for i in range(N):
        for j in range(N):
            if cluster[i][j] == 0:
                cluster, cluster_num, total_sum, total_num = DFS(cluster, cluster_num, i, j)
                

    if cluster_num == 1:
        break

    cnt += 1
print(cnt)
                


