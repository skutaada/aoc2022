f = open("input.txt", 'r')

c1 = 0
c2 = 0

for l in f:
  l = l.strip()
  l1, l2 = l.split(',')[0], l.split(',')[1]
  r11, r12 = int(l1.split('-')[0]), int(l1.split('-')[1])
  r21, r22 = int(l2.split('-')[0]), int(l2.split('-')[1])
  r1 = range(r11, r12+1)
  r2 = range(r21, r22+1)
  if all([r in r1 for r in r2]) or all([r in r2 for r in r1]):
    c1 += 1
  if any([r in r1 for r in r2]) or any([r in r2 for r in r1]):
    c2 += 1

print(c1, c2)
