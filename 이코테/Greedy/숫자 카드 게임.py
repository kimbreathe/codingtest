N, M = map(int, input().split()) # N*M 배열
minimum = []

for i in range(N):
  arr = list(map(int, input().split()))
  minimum.append(min(arr))

print(max(minimum))