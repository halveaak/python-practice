def pyramid(layers):
  bricks = (layers * (layers + 1) * (2* layers +1)) // 6
  return bricks
