import unittest
import solution

class SolutionTest(unittest.TestCase):
  def test1(self):
    test_input = 4
    self.assertEqual(solution.solution(test_input), 2)

  def test2(self):
    test_input = 15
    self.assertEqual(solution.solution(test_input), 5)

  def test3(self):
    test_input = 1023
    self.assertEqual(solution.solution(test_input), 11)

  def test4(self):
    test_input = 8190
    self.assertEqual(solution.solution(test_input), 14)

  def test5(self):
    test_input = 90876551
    self.assertEqual(solution.solution(test_input), 38)

  def test6(self):
    test_input = (1 << 309) - 1
    self.assertEqual(solution.solution(test_input), 310)

  def test7(self):
    x = 0
    for i in xrange(309):
      x = x << 1
      if i % 2 == 0:
        x += 1
    test_input = x
    self.assertEqual(solution.solution(test_input), 462)

if __name__ == '__main__':
  unittest.main()
