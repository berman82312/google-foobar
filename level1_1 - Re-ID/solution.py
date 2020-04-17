def solution(i):
  # start/end index of the id string
  start = i
  end = i + 5
  # initial setup
  prime_str = '23571113'
  prime_list = [2,3,5,7,11,13]
  max_prime = 13
  max_length = 8
  while max_length < end:
    current = max_prime + 2
    is_prime = False
    while not is_prime:
      is_prime = True
      for prime in prime_list:
        rest = current % prime
        if rest == 0:
          is_prime = False
          break
      if is_prime:
        max_prime = current
        prime_list.append(current)
        current = str(current)
        max_length += len(current)
        prime_str += current
      else:
        current += 2
  return prime_str[start:end]
