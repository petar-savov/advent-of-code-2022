with open('input1.txt') as f:
    calories = [l.strip() for l in f.readlines()]


elves = [0]
for item in calories:
    if item == '':
        elves.append(0)
    else:
        elves[-1] += int(item)

print(max(elves))
print(sum(sorted(elves)[-3:]))
