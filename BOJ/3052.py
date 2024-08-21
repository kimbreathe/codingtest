# 3052 나머지
# 10 개의 입력값을 42로 나눈 나머지 중 서로 다른 것의 개수

rest = []

for i in range(10):
  n = int(input())
  rest.append(n%42)

print(len(set(rest)))