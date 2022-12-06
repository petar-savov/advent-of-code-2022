s <- readChar("input6.txt", file.info("input6.txt")$size)
s <- strsplit(s, "")[[1]]

check <- function(n) {
  for (i in seq(n, length(s))) {
    if (length(unique(s[i-n+1:n])) == n) {
      return (i)
    }
  }  
}

print(check(4))
print(check(14))