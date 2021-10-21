def calculate(left, right, operation):
    if operation == '0': # + 
        return left+right
    elif operation == '1': # -
        return left-right
    elif operation == '2': # *
        return left*right
    else:               # /
        if left*right < 0: 
            return - (abs(left) // abs(right))
        else:
            return int(left // right)            

def operations_perm(perms, operations):
    if sum(operations) == 0:
        return perms
    
    total_returns = []
    for i in range(4):
        returns = []
        if operations[i] > 0:
            for p in perms:
                returns.append(p+str(i))
                operations[i] -= 1
                total_returns.extend(operations_perm(returns, operations))
                operations[i] += 1

    return total_returns


def operate(perm):
    left = As[0]
    for i in range(N-1):
        right = As[i+1]
        left = calculate(left, right, perm[i])

    print("CALCULATE")
    print(left)
    print_perm(perm)
    return left

def print_perm(perm):
    perm_str = ["+", "-", "x", "/"]
    line = str(As[0])
    for i in range(N-1):
        line += perm_str[int(perm[i])] + str(As[i+1])
    print(line)


N= int(input())
As = list(map(int, input().split()))
operations = list(map(int, input().split())) # + - x /
total_perms = operations_perm([""], operations)
min_v = None; max_v = None

for perm in total_perms:
    v = operate(perm)
    if min_v == None:
        min_v = v
        max_v = v
    else:
        min_v = min(min_v, v)
        max_v = max(max_v, v)
print(max_v)
print(min_v)
