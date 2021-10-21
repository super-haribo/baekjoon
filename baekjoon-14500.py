N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_v = 0

# shape (1*4) (2*2) (2*3 중 4개)

def print_t(shape):
    for r in shape:
        print(r)
    print("\n")

for n, m in [(1, 4), (4, 1), (2, 2)]:
    for i in range(N-n+1):
        for j in range(M-m+1):
            area = [r[j:j+m] for r in board[i:i+n]]
            v = 0
            for r in area:
                v+=sum(r)
            
            assert len(area) == 4 or len(area[0]) == 4 or (len(area[0])== 2 and len(area)==2)
            max_v = max(max_v, v)

for n, m in [(3, 2)]:
    for i in range(N-n+1):
        for j in range(M-m+1):
            area = [[k for k in r[j:j+m]] for r in board[i:i+n]]

            # 1 0
            # 1 0
            # 1 1
            v = sum([area[0][0], area[1][0], area[2][0]]) + max([area[0][1], area[1][1], area[2][1]])
            max_v = max(max_v, v)
            
            # 0 1
            # 1 1
            # 0 1
            v = sum([area[0][1], area[1][1], area[2][1]]) + max([area[0][0], area[1][0], area[2][0]])
            max_v = max(max_v, v)

            # 0 1
            # 1 1 
            # 1 0            
            v = sum(area[1]) + max(area[0]) + max(area[2]) 
            max_v = max(max_v, v)


for n, m in [(2, 3)]:
    '''
    [[ 1 0 1]
     [ 0 1 1]]
    '''
    for i in range(N-n+1):
        for j in range(M-m+1):
            area = [[k for k in r[j:j+m]] for r in board[i:i+n]]

            # (1)
            v = sum(area[0]) + sorted(area[1])[-1]
            max_v = max(max_v, v)

            # (2)
            v = sum(area[1]) + sorted(area[0])[-1]
            max_v = max(max_v, v)

            # (3)
            v = sum([area[0][1], area[1][1]]) + max([area[0][0], area[1][0]]) +  max([area[0][2], area[1][2]]) 
            max_v = max(max_v, v)

print(max_v)

'''
5 5
0 0 7 8 9
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
-> 25

5 5 
0 0 0 0 0
0 1 7 8 9
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
-> 25

5 5
0 0 0 0 0
0 1 0 0 0
0 7 0 0 0
0 8 2 0 0
0 9 0 0 0
-> 26

2 3 
1 0 1
0 1 1
-> 3

2 4
3 2 1 1
0 1 4 3
-> 10

3 2
4 1
4 0 
4 0 
->13

3 2
4 0
4 4
0 4
-> 16

3 3 
4 4 0
0 0 0
4 4 0
-> 12

3 3
0 4 4 
0 4 4 
0 0 0
-> 16

4 4 
7 4 4 4
20 0 0 0
7 3 3 3 
7 5 5 5
-> 41

'''