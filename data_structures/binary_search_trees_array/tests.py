import unittest

from binary_search_tree_array import aBST


class TestBSTree(unittest.TestCase):

    def setUp(self):
        self.tree = aBST(2)

    def test(self):
        print(self.tree.Tree)


if __name__ == '__main__':
    unittest.main()
