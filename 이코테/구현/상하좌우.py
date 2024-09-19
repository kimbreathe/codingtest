N = int(input())
move = input().split() # 리스트로 저장

# 시작 위치
x, y = 1, 1

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(len(move)):
  S = move[i]
  if S == 'L':
    if y <= 1:
      continue
    y += dy[2]
  elif S == 'R':
    if y >= N:
      continue
    y += dy[0]
  elif S == 'U':
    if x <= 1:
      continue
    x += dx[1]
  else:
    if x >= N:
      continue
    x += dx[3]

print(x, y)