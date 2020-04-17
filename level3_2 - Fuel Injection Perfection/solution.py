def solution(n):
  x = int(n)
  if (x == 1):
    return 0
  step_count = 0
  while x > 1:
    # 3 is a special case
    if (x == 3):
      step_count += 2
      break
    if (x & 1) == 0:
      x = x >> 1
    else:
      # Select between add 1 or minus 1 on which could have more zeros
      a = x + 1
      b = x - 1
      a_count = 0
      b_count = 0
      while (a & 1) == 0:
        a_count += 1
        a = a >> 1
      while (b & 1) == 0:
        b_count += 1
        b = b >> 1
      if (a_count > b_count):
        x = a
        step_count += a_count
      else:
        x = b
        step_count += b_count
    step_count += 1
  return step_count
