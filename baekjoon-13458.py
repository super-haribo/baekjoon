N = int(input())
As = list(map(int, input().split()))
B, C = map(int, input().split())

num = 0
for Ai in As:
    num += 1; Ai -= B # 총감독관
    if Ai <= 0:
        continue
    
    num += Ai // C + (0 if Ai%C == 0 else 1) # 부감독관

print(num)