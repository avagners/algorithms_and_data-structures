import unittest

from binary_search_tree import BSTNode, BSTFind, BST


class TestEmptyTree(unittest.TestCase):

    def setUp(self):
        self.tree = BST(None)

    def test_tree(self):
        self.assertIsInstance(self.tree, BST)
        self.assertIsNone(self.tree.Root)

    def test_node(self):
        node = BSTNode(key=1, val=1, parent=None)
        self.assertIsInstance(node, BSTNode)
        self.assertEqual(node.NodeKey, 1)
        self.assertEqual(node.NodeValue, 1)
        self.assertIsNone(node.Parent)

    def test_find_node(self):
        search_result = self.tree.FindNodeByKey(1)
        self.assertIsInstance(search_result, BSTFind)
        self.assertIsNone(search_result.Node)
        self.assertFalse(search_result.ToLeft)
        self.assertFalse(search_result.NodeHasKey)

    def test_add_root_node(self):
        self.assertIsNone(self.tree.FindNodeByKey(10).Node)
        self.tree.AddKeyValue(10, 1)
        self.assertIsNotNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsInstance(self.tree.Root, BSTNode)
        self.assertEqual(self.tree.Root.NodeKey, 10)
        self.assertEqual(self.tree.Root.NodeValue, 1)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)

    def test_add_many_nodes(self):
        self.assertIsNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsNone(self.tree.FindNodeByKey(8).Node)
        self.assertIsNone(self.tree.FindNodeByKey(12).Node)
        self.tree.AddKeyValue(10, 1)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        self.assertIsNotNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsNotNone(self.tree.FindNodeByKey(8).Node)
        self.assertIsNotNone(self.tree.FindNodeByKey(12).Node)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsInstance(self.tree.Root.LeftChild, BSTNode)
        self.assertIsInstance(self.tree.Root.RightChild, BSTNode)
        self.assertLess(
            self.tree.Root.LeftChild.NodeKey, self.tree.Root.NodeKey
        )
        self.assertGreater(
            self.tree.Root.RightChild.NodeKey, self.tree.Root.NodeKey
        )
        self.assertEqual(
            self.tree.Root.LeftChild.Parent.NodeKey, self.tree.Root.NodeKey
        )
        self.assertEqual(
            self.tree.Root.RightChild.Parent.NodeKey, self.tree.Root.NodeKey
        )

    def test_add_identical_keys(self):
        self.assertIsNone(self.tree.FindNodeByKey(10).Node)
        self.tree.AddKeyValue(10, 1)
        self.assertIsNotNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)
        self.assertEqual(self.tree.Root.NodeValue, 1)
        self.assertEqual(self.tree.Root.NodeKey, 10)
        # проверка, что при попытке добавить узел с таким же ключом
        # дерево не изменяется
        self.tree.AddKeyValue(10, 2)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)
        self.assertEqual(self.tree.Root.NodeValue, 1)
        self.assertEqual(self.tree.Root.NodeKey, 10)

    def test_find_min_max(self):
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertIsNone(result)
        self.tree.AddKeyValue(10, 1)
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(result.NodeKey, 10)
        result = self.tree.FinMinMax(self.tree.Root, False)
        self.assertEqual(result.NodeKey, 10)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(result.NodeKey, 12)
        result = self.tree.FinMinMax(self.tree.Root, False)
        self.assertEqual(result.NodeKey, 8)
        result = self.tree.FinMinMax(self.tree.Root.LeftChild, True)
        self.assertEqual(result.NodeKey, 8)
        result = self.tree.FinMinMax(self.tree.Root.RightChild, False)
        self.assertEqual(result.NodeKey, 12)
        self.tree.AddKeyValue(5, 4)
        self.tree.AddKeyValue(16, 5)
        result = self.tree.FinMinMax(self.tree.Root, False)
        self.assertEqual(result.NodeKey, 5)
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(result.NodeKey, 16)

    def test_get_count(self):
        self.assertEqual(self.tree.Count(), 0)
        self.tree.AddKeyValue(10, 1)
        self.assertEqual(self.tree.Count(), 1)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        self.assertEqual(self.tree.Count(), 3)


if __name__ == '__main__':
    unittest.main()
