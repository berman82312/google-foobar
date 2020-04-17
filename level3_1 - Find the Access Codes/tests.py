import unittest
import solution

class SolutionTest(unittest.TestCase):
  def test1(self):
    test_input = [1, 1, 1]
    self.assertEqual(solution.solution(test_input), 1)

  def test2(self):
    test_input = [1, 2, 3, 4, 5, 6]
    self.assertEqual(solution.solution(test_input), 3)

  def test3(self):
    test_input = [1, 5, 6, 13, 17, 121]
    self.assertEqual(solution.solution(test_input), 0)

  def test4(self):
    test_input = [1, 1, 2, 2, 4, 4, 8, 8, 12, 16, 16]
    self.assertEqual(solution.solution(test_input), 135)

  def test5(self):
    test_input = range(1, 2001)
    self.assertEqual(solution.solution(test_input), 40888)

if __name__ == '__main__':
  unittest.main()
