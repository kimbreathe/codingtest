N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0 # 현재 그룹의 인원
result = 0 # 그룹의 수

for i in arr:
  cnt += 1
  if cnt >= i:
    cnt = 0
    result += 1

print(result)