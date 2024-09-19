location = input()

# a1 = 열 행
col = ord(location[0]) - ord('a') + 1
row = int(location[1])

cnt = 0

move = [(-1, -2), (-1, 2),
        (-2, -1), (-2, 1),
        (1, -2), (1, 2),
        (2, -1), (2, 1)]

for i in move:
  nc = col + i[0]
  nr = row + i[1]
  if nc < 1 or nc > 8 or nr < 1 or nr > 8:
    continue
  cnt += 1

print(cnt)