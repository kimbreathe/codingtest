# 10813 공 바꾸기

N, M = map(int, input().split())
basket = [b for b in range(1, N+1)]

for _ in range(M):
  i, j = map(int, input().split())
  tmp = basket[i-1]
  basket[i-1] = basket[j-1]
  basket[j-1] = tmp

print(*basket)