import sys

N = int(sys.stdin.readline())
C, S = 100, 100

for _ in range(N):
  # 창영이 C 상덕이 S
  c, s = map(int, sys.stdin.readline().split())
  if c < s:  # 상덕이가 이겼을 때
    C -= s
  elif c > s:  # 창영이가 이겼을 때
    S -= c
  else:
    continue

print(C)
print(S)
