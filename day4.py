import re

with open("input4.txt") as f:
    lines = f.readlines()

nums = [[int(d) for d in line] for line in [re.findall("\d+", l) for l in lines]]
s1, s2 = 0, 0
for a, b, c, d in nums:
    if (a >= c and b <= d) or (c >= a and d <= b):
        s1 += 1
    if (b >= c and a <= d) or (d >= a and d <= b):
        s2 += 1

print(s1, s2)
