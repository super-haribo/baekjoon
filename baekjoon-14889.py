N= int(input())
scores = [list(map(int, input().split())) for _ in range(N)]

def calculate(team):
    M = len(team); score = 0
    for i in range(M-1):
        for j in range(i+1, M):
            x = team[i]; y = team[j]
            score += scores[x][y] + scores[y][x]
    return score

def make_team(team):
    if len(team) == N//2:
        return [",".join([str(s) for s in team])]

    min_idx = team[-1] + 1
    if (N-1) - min_idx + 1 < N//2 - len(team):
        return []

    returns = []    
    for cand in range(min_idx, N):
        r = make_team(team+[cand])
        if len(r) > 0:
            returns.extend(r)
    
    return returns

team_candidates = make_team([0])
min_v = None
for team1 in team_candidates:
    team1 = list(map(int, team1.split(",")))

    team2 = list(set(range(N)) - set(team1))

    team1_score = calculate(team1)
    team2_score = calculate(team2)

    diff = abs(team1_score - team2_score)
    if min_v == None:
        min_v = diff
    else:
        min_v = min(min_v, diff)

print(min_v)
# print(len(team_candidates))
# for i in range(1, N-1):
#     line = ""
#     for t in team_candidates:
#         if t[2] == str(i):
#             line += t + " "
#     print(i, "=>", line)

'''
(0, 1) -> 6C2 = 15
(0, 2) -> 5C2 = 10 
(0, 3) -> 4C2 = 6
(0, 4) -> 3C2 = 3
(0, 5) -> 2C2 = 1
7C3 = 7*6*5/6 = 35
'''

