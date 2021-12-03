library(magrittr)
bits <- readLines('input.txt')

vecToStr <- function(v) v %>% as.character() %>% paste0(collapse = '')

lineToRow <- function(l) {
  vec <- strsplit(l, split = '')[[1]]
  matrix(as.numeric(vec), 1, length(vec))
}

X <- sapply(bits, lineToRow) %>% unname() %>% t()

gamma_int <- X %>% colMeans() %>% round()
epsilon_int <- 1 - gamma_int

gamma <- vecToStr(gamma_int)
epsilon <- vecToStr(epsilon_int)

res_a <- strtoi(gamma, base = 2)*strtoi(epsilon, base = 2)

O2 <- X
for (d in 1:ncol(O2)) {
  n <- nrow(O2)
  n1 <- sum(O2[,d])
  mode <- (2*n1 >= n)*1
  O2 <- O2[O2[, d] == mode, , drop = FALSE]
  if (nrow(O2) == 1) break
}

O2_bin <- vecToStr(O2)

CO2 <- X
for (d in 1:ncol(CO2)) {
  n <- nrow(CO2)
  n1 <- sum(CO2[,d])
  mode <- (2*n1 >= n)*1
  CO2 <- CO2[CO2[, d] == 1 - mode, , drop = FALSE]
  if (nrow(CO2) == 1) break
}

CO2_bin <- vecToStr(CO2)

res_b <- strtoi(O2_bin, base = 2)*strtoi(CO2_bin, base = 2)

cat("A ::: Power consumption =", res_a, '\n')
cat("B ::: Life support rating =", res_b, '\n')
