import unittest
import core

class TestStringMethods(unittest.TestCase):


  def test_reverse(self):
      self.assertEqual(core.reverse('123'),'3221')


if __name__ == '__main__':
    unittest.main()
