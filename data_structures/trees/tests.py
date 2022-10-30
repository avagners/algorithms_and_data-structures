import unittest

from SimpleTree import SimpleTree, SimpleTreeNode


class TestSimpleTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tree = SimpleTree(None)

    def setUp(self):
        self.node_root = SimpleTreeNode(6, None)
        self.new_node_2 = SimpleTreeNode(7, self.node_root)
        self.new_node_3 = SimpleTreeNode(8, self.node_root)
        self.new_node_4 = SimpleTreeNode(8, self.new_node_3)
        self.tree.AddChild(None, self.node_root)
        self.tree.AddChild(self.node_root, self.new_node_2)
        self.tree.AddChild(self.node_root, self.new_node_3)
        self.tree.AddChild(self.new_node_3, self.new_node_4)

    def test_add_node(self):
        self.assertEqual(self.tree.Count(), 4)
        new_node = SimpleTreeNode(10, self.node_root)
        self.tree.AddChild(self.node_root, new_node)
        self.assertEqual(self.tree.Count(), 5)
        self.assertIn(new_node, self.node_root.Children)
        self.assertEqual(new_node.Parent, self.node_root)

    def test_FindNodesByValue(self):
        find_nodes = self.tree.FindNodesByValue(8)
        self.assertEqual(find_nodes, [self.new_node_3, self.new_node_4])

    def test_Count(self):
        self.assertEqual(self.tree.Count(), 4)
        new_node = SimpleTreeNode(10, self.node_root)
        self.tree.AddChild(self.node_root, new_node)
        self.assertEqual(self.tree.Count(), 5)

    def test_LeafCount(self):
        self.assertEqual(self.tree.LeafCount(), 2)
        new_leaf = SimpleTreeNode(10, self.node_root)
        self.tree.AddChild(self.node_root, new_leaf)
        self.assertEqual(self.tree.LeafCount(), 3)
        new_leaf_2 = SimpleTreeNode(10, self.new_node_3)
        self.tree.AddChild(self.new_node_3, new_leaf_2)
        self.assertEqual(self.tree.LeafCount(), 4)
        new_not_leaf = SimpleTreeNode(11, self.new_node_2)
        self.tree.AddChild(self.new_node_2, new_not_leaf)
        self.assertEqual(self.tree.LeafCount(), 4)

    def test_DeleteNode(self):
        self.assertEqual(self.tree.Count(), 4)
        self.tree.DeleteNode(self.new_node_3)
        # проверяем кол-во узлов после удаления
        self.assertEqual(self.tree.Count(), 2)
        # проверяем отсутсвие удаленного узла в
        # списке Children родительского узла
        self.assertNotIn(self.new_node_3, self.tree.Root.Children)
        # проверяем отсутсвие удаленного узла и
        # всех его дочерних узлов в дереве
        self.assertNotIn(self.new_node_3, self.tree.GetAllNodes())
        self.assertNotIn(self.new_node_4, self.tree.GetAllNodes())


if __name__ == '__main__':
    unittest.main()
