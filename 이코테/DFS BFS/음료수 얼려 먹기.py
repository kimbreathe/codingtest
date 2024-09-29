N, M = map(int, input().split())
ice = []

# 얼음틀 입력받기 (리스트로 받을거라서 .split()은 안해도 됨)
for i in range(N):
    ice.append(list(map(int, input().split())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    # 노드가 0일 때만 상하좌우 재귀 검사
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y) #상
        dfs(x+1, y) #하
        dfs(x, y-1) #좌
        dfs(x, y+1) #우
        return True
    # 노드가 1이면 False 반환
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)