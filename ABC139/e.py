# encodin: utf-8

N=int(input())
A=[list(map(lambda x: int(x)-1,  input().split())) for _ in range(N)]
#選手を0から採番したい

print(A)

q = []
game = []

#iの次の組み合わせをキューに追加
def check(i):
    if len(A[i]) == 0:
        return

    #対戦相手
    j = A[i][0]

    if A[j][0] == i:
        game = [i, j] if i < j else [j, i] 
        if q.count(game) == 0:
            q.append(game) 

#初期化(第1試合のリスト)
for i in range(N):
    check(i)

day=0

prev_q = []
while len(q) > 0:
    day += 1

    prev_q = q
    q = []

    for game in prev_q:
        i = game[0]
        j = game[1]

        #消化した対戦を消す
        A[i].pop(0)
        A[j].pop(0)

        #試合をした人の次の試合をキューに積む
        check(i)
        check(j)

#対戦リストが残っちゃったら無理な組み合わせだった
for a in A:
    if len(a) > 0:
        print(-1)
        exit()

print(day)

