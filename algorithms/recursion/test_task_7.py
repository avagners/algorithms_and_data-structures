import unittest

from task_7 import main


class Tests(unittest.TestCase):

    def test_1(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        result = main(array)
        self.assertEqual(result, 6)

    def test_2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 7, 7]
        result = main(array)
        self.assertEqual(result, 7)

    def test_3(self):
        array = [6, 6, 7]
        result = main(array)
        self.assertEqual(result, 6)

    def test_4(self):
        array = [5, 4, 3, 2, 5]
        result = main(array)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
