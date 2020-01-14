n = int(input())

town = [list(map(int, input().split())) for _ in range(n)]

distance = [[0]*n for _ in range(n)]
    
for i in range(n):
    for j in range(i,n):
        d = ( (town[i][0] - town[j][0])**2 + (town[i][1] - town[j][1])**2 ) ** 0.5
        distance[i][j] = d
        distance[j][i] = d

print(sum(map(sum, distance)) / n )
