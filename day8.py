with open("input8.txt") as f:
    lines = [[int(d) for d in line.strip()] for line in f.readlines()]


rows = len(lines)
cols = len(lines[0])


def get_los(i, j):
    return [
        lines[i][:j][::-1],
        lines[i][j + 1 :],
        [l[j] for l in lines[:i]][::-1],
        [l[j] for l in lines[i + 1 :]],
    ]


# part 1

vis = rows * 2 + cols * 2 - 4
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        lines_of_sight = get_los(i, j)
        vis += any(all(d < lines[i][j] for d in los) for los in lines_of_sight)

print(vis)

# part 2

best_score = 0
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        lines_of_sight = get_los(i, j)
        score = 1
        for l in lines_of_sight:
            line_score = 0
            for d in l:
                line_score += 1
                if d >= lines[i][j]:
                    break
            score *= line_score
        best_score = max(best_score, score)

print(best_score)
