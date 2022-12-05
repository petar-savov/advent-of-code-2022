import re

with open("input5.txt") as f:
    crates, ins = f.read().split("\n\n")

crates = crates.splitlines()[:-1]
ins = [[int(d) for d in re.findall("\d+", line)] for line in ins.strip().split("\n")]


def parse(crates):
    stacks = []
    for i in range(1, 35, 4):
        stack = [c[i] for c in crates[:-1] if c[i] != " "]
        stacks.append(stack[::-1])
    return stacks


# part 1
stacks = parse(crates)
for n, from_, to in ins:
    for _ in range(n):
        stacks[to - 1].append(stacks[from_ - 1].pop())

print("".join(s.pop() for s in stacks))

# part 2
stacks = parse(crates)
for n, from_, to in ins:
    cutoff = len(stacks[from_ - 1]) - n
    stacks[to - 1].extend(stacks[from_ - 1][cutoff:])
    stacks[from_ - 1] = stacks[from_ - 1][:cutoff]

print("".join(s[-1] for s in stacks if s))
