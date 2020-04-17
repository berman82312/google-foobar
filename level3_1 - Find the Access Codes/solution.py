def solution(l):
  length = len(l)
  if length < 3:
    return 0
  divides_count = [0]
  triple_count = 0
  for j in xrange(1, length):
    count = 0
    for i in xrange(j):
      if l[j] % l[i] == 0:
        count += 1
        triple_count += divides_count[i]
    divides_count.append(count)
  return triple_count
