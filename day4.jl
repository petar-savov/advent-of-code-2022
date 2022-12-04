f = open("input4.txt")
data = readlines(f)
close(f)

struct Elf
    s::Int
    f::Int
end

function contains(elf, another)
    return elf.s <= another.s && elf.f >= another.f
end

function overlaps(elf, another)
    return (elf.f >= another.s && elf.s <= another.f) || (another.f >= elf.s && another.f <= elf.f)
end

p1, p2 = [], []
for line in data
    elves = [split(e, "-") for e in split(line, ",")]
    e1 = Elf(parse(Int, elves[1][1]), parse(Int, elves[1][2]))
    e2 = Elf(parse(Int, elves[2][1]), parse(Int, elves[2][2]))

    append!(p1, contains(e1, e2) | contains(e2, e1))
    append!(p2, overlaps(e1, e2))
end

println(sum(p1), "\n", sum(p2))
