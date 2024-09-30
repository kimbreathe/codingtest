# 백준 18352

import sys
from collections import deque
# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, sys.stdin.readline().split())

# 1번 도시부터 N번 도시 배열 초기화
graph = [[] for _ in range(N+1)]
#간선정보 입력
for _ in range(M):
  A, B = map(int, sys.stdin.readline().split())
  graph[A].append(B)

# 출발 도시로부터 거리를 저장
distance = [-1 for _ in range(N+1)]
distance[X] = 0

# BFS 시작
queue = deque()
queue.append(X)
  
while queue:
  v = queue.popleft()
  # 현재 도시에서 갈 수 있는 모든 도시
  for i in graph[v]:
    if distance[i] != -1:
      continue
    else:
      distance[i] = distance[v] + 1
      queue.append(i)

# 거리 정보 체크
check = False
for i in range(N+1):
  if distance[i] == K:
    check = True
    print(i)

if check == False:
  print(-1)