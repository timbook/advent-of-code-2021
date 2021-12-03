library(magrittr)

bits <- readLines('input.txt')

vecToStr <- function(v) v %>% as.character() %>% paste0(collapse = '')

lineToRow <- function(l) {
  vec <- strsplit(l, split = '')[[1]]
  matrix(as.numeric(vec), 1, length(vec))
}

colMode <- function(X) {
  n <- nrow(X)
  n1 <- sum(X[,d])
  (2*n1 >= n)*1
}

X <- sapply(bits, lineToRow) %>% unname() %>% t()

gamma_int <- X %>% colMeans() %>% round()
epsilon_int <- 1 - gamma_int

gamma <- vecToStr(gamma_int)
epsilon <- vecToStr(epsilon_int)

res_a <- strtoi(gamma, base = 2)*strtoi(epsilon, base = 2)

O2 <- X
for (d in 1:ncol(O2)) {
  O2 <- O2[O2[, d] == colMode(O2), , drop = FALSE]
  if (nrow(O2) == 1) break
}

CO2 <- X
for (d in 1:ncol(CO2)) {
  CO2 <- CO2[CO2[, d] == 1 - colMode(CO2), , drop = FALSE]
  if (nrow(CO2) == 1) break
}

O2_dec <- vecToStr(O2) %>% strtoi(base = 2)
CO2_dec <- vecToStr(CO2) %>% strtoi(base = 2)

res_b <- O2_dec*CO2_dec

cat("A ::: Power consumption =", res_a, '\n')
cat("B ::: Life support rating =", res_b, '\n')