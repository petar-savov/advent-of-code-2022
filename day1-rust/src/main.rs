use std::fs;
fn main() {
    let data = fs::read_to_string("../input1.txt").unwrap();
    let calories: Vec<&str> = data.split('\n').collect();
    let mut elves: Vec<i32> = vec![0];
    for c in calories {
        if c == "" {
            elves.push(0)
        } else {
            *elves.last_mut().unwrap() += c.parse::<i32>().unwrap()
        }
    }
    elves.sort();
    println!("{}", elves.last().unwrap());
    println!("{}", elves.iter().rev().take(3).sum::<i32>());
}
