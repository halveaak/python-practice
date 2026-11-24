def collatz(n):
  moves = 0
  while n > 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n= 3 * n + 1
    moves = moves + 1
  return moves