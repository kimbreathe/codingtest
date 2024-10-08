# 25206 너의 평점은

course = []
credit = []
score = []

Point = {
  'A+': 4.5,
  'A0': 4.0,
  'B+': 3.5,
  'B0': 3.0,
  'C+': 2.5,
  'C0': 2.0,
  'D+': 1.5,
  'D0': 1.0,
  'F': 0.0
}

for i in range(20):
  value = input().split()
  if value[2] == 'P':
    continue
  course.append(value[0])
  credit.append(float(value[1]))
  score.append(value[2])

avgscore = 0
avgscore = sum(credit[i] * Point[score[i]] for i in range(len(credit))) / sum(credit)

print(avgscore)