# encoding: utf-8
N,K,Q = map(int, input().split())

A=[int(input()) for _ in range(Q)]

#初期ポイント
points=[K for _ in range(N)]

# 問題数分、ポイントを引いてしまい、
# あとから正解者にポイントを足す
points=list(map(lambda x: x - Q, points))

for a in A:
    points[a-1] += 1

#print(list(map(lambda x: 'Yes' if x > 0 else 'No', points)))

for point in points:
    print('Yes' if point > 0 else 'No')
