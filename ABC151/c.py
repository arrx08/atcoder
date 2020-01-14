n,m = map(int, input().split())

solved = set()
correct = 0
penalty = 0
penalty_memo = [0] * (n+1)

for _ in range(m):
    p,s = input().split()
    p = int(p)

    if p not in solved:
        if s == "WA":
            penalty_memo[p] += 1
        else:
            correct += 1
            penalty += penalty_memo[p]
            solved.add(p)

print(correct, penalty)