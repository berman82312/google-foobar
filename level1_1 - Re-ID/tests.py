import unittest
import solution

class SolutionTest(unittest.TestCase):
  def test1(self):
    self.assertEqual('23571', solution.solution(0))

  def test2(self):
    self.assertEqual('71113', solution.solution(3))

  def test3(self):
    self.assertEqual('74143', solution.solution(19))

  def test4(self):
    self.assertEqual('93974', solution.solution(201))

  def test5(self):
    self.assertEqual('91009', solution.solution(4758))

  def test6(self):
    self.assertEqual('02192', solution.solution(10000))

if __name__ == '__main__':
  unittest.main()
