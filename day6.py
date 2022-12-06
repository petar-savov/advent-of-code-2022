with open("input6.txt") as f:
    s = f.read().strip()


def check(n):
    for i in range(n, len(s)):
        if len(set(s[i - n : i])) == n:
            return i


print(check(4), check(14))
