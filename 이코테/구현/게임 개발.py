# 해당 코드는 해설을 일부 참고하며 푼 코드입니다.

N, M = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문한 좌표 초기화
d = [[0] * M for _ in range(N)]
d[x][y] = 1

# map 생성
array = []
for i in range(N):
  array.append(list(map(int, input().split())))

# 방향 정의 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 회전 함수 정의
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
  turn_left()
  # 탐색할 칸의 위치 nx, ny
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 가보지 않은 칸+육지이면 이동!
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1

  # 네 방향 모두 갈 수 없는 경우(이미 동서남북 다 확인했으면?)
  if turn_time == 4:
    # 현재 위치에서 뒤쪽 탐색
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 육지면 이동, 바다면 break
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)