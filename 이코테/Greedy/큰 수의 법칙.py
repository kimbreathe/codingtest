N, M, K = map(int, input().split())
num = list(map(int, input().split()))
result = 0

num.sort() # 오름차순
first = num[-1]
second = num[-2]

cnt = M//(K+1)
rest = M%(K+1)

result += cnt*(first*K+second)
result += rest*first

print(result)