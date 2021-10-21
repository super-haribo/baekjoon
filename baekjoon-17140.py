R, C, K = map(int, input().split()); R-=1; C-=1
arr = [list(map(int, input().split())) for _ in range(3)]

def print_arr():
    global arr
    for r in arr:
        print(r)
    print("\n")

def get_new_list(arr):
    # 1. 횟수가 커지는 순서 2. 수가 커지는 순서
    arr_dict = {}
    for v in arr:
        if v not in arr_dict:
            arr_dict[v] = 0 
        arr_dict[v] += 1

    if 0 in arr_dict:
        arr_dict.pop(0)

    arr_pair = [(k, arr_dict[k]) for k in arr_dict]
    arr_pair.sort(key = lambda x : (x[1], x[0]))

    new_arr = []
    for r, c in arr_pair:
        new_arr.append(r)
        new_arr.append(c)
    
    return new_arr

def pad_row(mat, max_l):
    for idx, row in enumerate(mat):
        if len(row) == max_l:
            continue

        mat[idx] = row + [0 for _ in range(max_l - len(row))]
    return mat

def operation_R():
    global arr

    rows = []; max_len = 0
    for r_idx in range(len(arr)):
        row = arr[r_idx]
        new_row = get_new_list(row)
        rows.append(new_row)

        max_len = max(max_len, len(new_row))
    
    arr = pad_row(rows, max_len)


def transpose():
    global arr
    arr = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]


def operation_C():
    global arr
    cols = []; max_len = 0
    for c_idx in range(len(arr[0])):
        col = [row[c_idx] for row in arr]
        new_col = get_new_list(col)
        cols.append(new_col)

        max_len = max(max_len, len(new_col))

    arr = pad_row(cols, max_len)

    # transpose
    transpose()


def operation():
    global arr
    cnt = 0

    while not (len(arr) > R and len(arr[0]) > C and arr[R][C] == K):

        if cnt == 101:
            break

        num_row = len(arr)
        col_row = len(arr[0])

        if num_row >= col_row:
            operation_R()
        else:
            operation_C()

        cnt += 1 

    if (cnt == 101):
        print(-1)
    else:
        print(cnt)



operation()