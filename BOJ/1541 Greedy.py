# 1541 잃어버린 괄호

import sys

exp = sys.stdin.readline().rstrip().split('-')

num = []

for i in range(len(exp)):
  sum = 0
  tmp = exp[i].split('+')
  for j in tmp:
    sum += int(j)
  num.append(sum)

result = num[0]
for k in range(1, len(num)):
  result -= num[k]

print(result)