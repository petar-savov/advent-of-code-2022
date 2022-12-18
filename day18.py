with open("input18.txt") as f:
    droplets = [[int(d) for d in line.split(",")] for line in f.readlines()]


def contact(a, b):
    eq, off_by_one = 0, 0
    for i in range(3):
        if a[i] == b[i]:
            eq += 1
        elif abs(a[i] - b[i]) == 1:
            off_by_one += 1

    return eq == 2 and off_by_one == 1


cnt = 0
track = set()
for i, d in enumerate(droplets):
    cnt += 6
    for j, f in enumerate(droplets[i:], i):
        if contact(d, f):
            sig = str(sorted([i, j]))
            if sig not in track:
                track.add(sig)
                cnt -= 2

print(cnt)
