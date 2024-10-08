# 1260 DFS와 BFS

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

# 그래프 입력받기
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for row in graph:
  row.sort()

# 방문노드 체크 및 초기화
visited = [False] * (n+1)
def init_v(visited):
  visited[:] = [False] * (n+1)

# 깊이 우선 탐색
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(graph, i, visited)

# 너비 우선 탐색
def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    x = queue.popleft()
    print(x, end = ' ')
    for i in graph[x]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


dfs(graph, v, visited)
init_v(visited)
print()
bfs(graph, v, visited)