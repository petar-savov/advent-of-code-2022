package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func main() {
	f, _ := os.Open("input3.txt")
	defer f.Close()
	scanner := bufio.NewScanner(f)
	var data []string
	for scanner.Scan() {
		line := scanner.Text()
		data = append(data, line)
	}

	// part 1
	p := 0
	for _, bag := range data {
		mid := len(bag) / 2
		var common rune
		c1, c2 := bag[:mid], bag[mid:]
		for _, i := range c1 {
			for _, j := range c2 {
				if i == j {
					common = i
				}
			}
		}
		p += score(common)
	}
	fmt.Println(p)

	// part 2
	p = 0
	for i := 0; i < len(data); i += 3 {
		var common rune
		for _, a := range data[i] {
			for _, b := range data[i+1] {
				for _, c := range data[i+2] {
					if a == b && b == c {
						common = a
					}
				}
			}
		}
		p += score(common)
	}
	fmt.Println(p)
}

func score(s rune) int {
	if unicode.IsLower(s) {
		return int(s) - int('a') + 1
	}
	return int(s) - int('A') + 27
}
