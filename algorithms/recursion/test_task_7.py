import random
import unittest

from task_7 import find_second_max


class TestDequeOneItem(unittest.TestCase):

    def test_1(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        result = find_second_max(array)
        self.assertEqual(result, 6)

    def test_2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 7, 7]
        result = find_second_max(array)
        self.assertEqual(result, 6)

    def test_3(self):
        array = [6, 6, 7]
        result = find_second_max(array)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
