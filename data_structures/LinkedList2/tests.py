import random
import unittest

from LinkedList2 import LinkedList2, Node


class TestLinkedList2OneItem(unittest.TestCase):

    def setUp(self):
        self.s_list = LinkedList2()
        self.number = random.randint(0, 100)
        self.node = Node(self.number)
        self.s_list.add_in_tail(self.node)

    def test_one_item_check_head_tail_len_prev_next(self):
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, self.node)
        self.assertEqual(self.s_list.tail, self.node)
        self.assertIsNone(self.node.next)
        self.assertIsNone(self.node.prev)

    def test_one_item_add_in_tail(self):
        new_node = Node(random.randint(0, 100))
        self.s_list.add_in_tail(new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.head, self.node)
        self.assertEqual(self.s_list.tail, new_node)
        self.assertEqual(self.node.next, new_node)
        self.assertIsNone(self.node.prev)
        self.assertEqual(new_node.prev, self.node)
        self.assertIsNone(new_node.next)

    def test_one_item_find(self):
        result = self.s_list.find(self.number)
        self.assertIsInstance(result, Node)
        self.assertEqual(result, self.node)

    def test_one_item_len(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
