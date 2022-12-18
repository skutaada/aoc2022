letter_to_number = {chr(i): i - 96 for i in range(97, 123)}
letter_to_number.update({chr(i): i - 38 for i in range(65, 91)})

f = open('input.txt', 'r')

total1 = 0
total2 = 0
group = []

for l in f:
    l = l.strip()
    l1, l2 = l[:len(l)//2], l[len(l)//2:]
    common = set(l1).intersection(l2)
    for c in common:
        total1 += letter_to_number[c]
    group.append(l)
    if len(group) == 3:
        common = set(group[0]).intersection(group[1]).intersection(group[2])
        for c in common:
            total2 += letter_to_number[c]
        group = []


print(total1)
print(total2)