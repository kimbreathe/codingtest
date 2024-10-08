import sys

N, K = map(int, sys.stdin.readline().split())

coin = []
for _ in range(N): #O(N)
  x = int(sys.stdin.readline())
  coin.append(x)

cnt = 0
for i in range(N-1,-1, -1):
  if coin[i] <= K:
    x = K // coin[i]
    cnt += x
    K %= coin[i]

print(cnt)