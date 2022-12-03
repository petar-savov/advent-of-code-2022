with open("input3.txt") as f:
    bags = [line.strip() for line in f.readlines()]


def score(item: str):
    if item.islower():
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


# part 1
p = 0
for b in bags:
    comp1, comp2 = set(b[: len(b) // 2]), set(b[len(b) // 2 :])
    item = comp1.intersection(comp2)
    p += score(item.pop())

print(p)

# part 2
p = 0
for i in range(0, len(bags), 3):
    badge = set(bags[i]).intersection(set(bags[i + 1])).intersection(set(bags[i + 2]))
    p += score(badge.pop())

print(p)
