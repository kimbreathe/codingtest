# 9012 괄호

import sys

N = int(sys.stdin.readline())

for _ in range(N):
  str = sys.stdin.readline()
  stack = []
  for i in str:
    # 시작 괄호일 때는 스택에 추가
    if i == "(":
      stack.append(i)
    # 끝 괄호일 때는 스택에서 pop
    elif i == ")":
      if stack:
        stack.pop()
      else:
        # 만약 pop할 수 없다면 NO 출력
        print("NO")
        break
    # 반복문이 다 끝난 후 스택 검사
    else:
      if not stack:
        print("YES")
      else:
        print("NO")