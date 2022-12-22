import re

with open("input21.txt") as f:
    lines = [line.strip() for line in f.readlines()]


d = {}
while "root" not in d:
    for line in lines:
        monkey, instr = line.split(": ")
        number = re.findall("\d+", instr)
        if number:
            d[monkey] = int(number[0])
        else:
            a, op, b = instr.split()
            if a in d and b in d:
                a = str(d[a])
                b = str(d[b])
                d[monkey] = eval(a + op + b)

print(int(d["root"]))
