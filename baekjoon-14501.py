N = int(input())
day= [0]; pay =[0]
for _ in range(N):
    d, p = map(int, input().split())
    day.append(d); pay.append(p)

def SEARCH(today, earn):
    # print("TODAY", today, "->", earn)
    if today > N:
        return earn

    # IF NOT
    v_X = SEARCH(today+1, earn)

    end_day = today + day[today] - 1  
    if end_day > N:
        return v_X

    # IF DO
    v_O = SEARCH(end_day+1, earn+pay[today])

    return max(v_O, v_X)

print(SEARCH(1, 0))

'''
3
4 5
1 1
2 1

'''
    

