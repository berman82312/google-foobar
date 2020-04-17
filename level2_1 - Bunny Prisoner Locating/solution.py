def solution(x, y):
  result = 0
  if y == 1:
    result = (1 + x) * x / 2
  elif y == 2:
    result = (1 + x) * x / 2 + x
  else:
    end = x + y - 2
    result = (1 + end) * end / 2 + x
  return str(result)
