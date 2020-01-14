import heapq as hq

N,M=map(int, input().split())
A=list(map(int, input().split()))

#ヒープキューのために符号逆転
A=list(map(lambda x: x * (-1), A))
hq.heapify(A)

for _ in range(M):
    a = hq.heappop(A) * (-1)
    hq.heappush(A, a // 2 * (-1))

print(sum(A) * (-1))
