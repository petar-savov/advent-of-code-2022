const fs = require('fs')
data = fs.readFileSync('./input2.txt','utf-8')
data = data.split('\n')

total1 = 0
total2 = 0
for (i = 0; i < data.length-1; i++) {
    switch (data[i]) {
        case 'A X':
            total1 += 4
            total2 += 3
            break
        case 'A Y':
            total1 += 8
            total2 += 4
            break
        case 'A Z':
            total1 += 3
            total2 += 8
            break
        case 'B X':
            total1 += 1
            total2 += 1
            break
        case 'B Y':
            total1 += 5
            total2 += 5
            break
        case 'B Z':
            total1 += 9
            total2 += 9
            break
        case 'C X':
            total1 += 7
            total2 += 2
            break
        case 'C Y':
            total1 += 2
            total2 += 6
            break
        case 'C Z':
            total1 += 6
            total2 += 7
            break
    }
}

console.log(total1, total2)