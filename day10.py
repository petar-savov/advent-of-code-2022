from dataclasses import dataclass

with open("input10.txt") as f:
    inp = [line.strip() for line in f.readlines()]


@dataclass
class State:
    reg: int = 1
    cycle: int = 0
    signals: int = 0
    display: str = ""

    def add(self, val):
        for _ in range(2):
            self.tick()
        self.reg += val

    def noop(self):
        self.tick()

    def tick(self):
        self.cycle += 1
        vals = list(range(20, 221, 40))
        if self.cycle in vals:
            self.signals += self.reg * self.cycle

        self.draw()

    def draw(self):
        hpos = self.cycle % 40
        sprite = list(range(max(self.reg - 1, 0), min(self.reg + 1, 39) + 1))

        if hpos - 1 in sprite:
            self.display += chr(9608)
        elif hpos == 0:
            self.display += "\n"
        else:
            self.display += " "


state = State()
for line in inp:
    if line == "noop":
        state.noop()
    else:
        state.add(int(line.split()[1]))

print(state.signals)
print(state.display)
