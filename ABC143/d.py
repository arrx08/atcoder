n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)

ans = 0

#1番長い辺(a)は固定する
for i in range(n - 2):
    #2番目に長い辺(b)＝次に長い辺とする
    j = i + 1
    #3番目の長さの辺(c)＝リストの中で最短の辺からスタート
    k = n - 1

    while j < k:
        #b<a+c,c<a+b は自明。a<b+cを判定する。
        #満たす場合、このbにおいて、cまでの全ての要素は条件を満たす(cが小さいほうから攻めているから)
        if l[i] < l[j] + l[k]:
            ans += k - j
            j += 1
        #満たさない場合、cを次に長い辺として再度判定。
        else:
            k -= 1

print(ans)