class Node:
    def __init__(self, v):
        super().__init__()
        self.value = v
        self.prev = None
        self.next = None


class EmptyNode(Node):
    def __init__(self, v=None):
        super().__init__(v)


class DummyLinkedList2:
    def __init__(self):
        self.head = EmptyNode()
        self.tail = EmptyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        self.tail.prev = item
        item.next = self.tail

    def print_all_nodes(self):
        node = self.head.next
        while node.value:
            print(node.value, end=' => ')
            node = node.next

    def find(self, val):
        node = self.head.next
        while node.value:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head.next
        result = []
        while node.value:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head.next
        while node.value:
            if node.value != val:
                node = node.next
                continue
            node.prev.next = node.next
            node.next.prev = node.prev
            if not all:
                break
            node = node.next

    def insert(self, afterNode, newNode):
        node = self.head.next
        while node:
            if node == afterNode:
                break
            node = node.next
        if node is None:
            self.tail.prev.next = newNode
            newNode.prev = self.tail.prev
            self.tail.prev = newNode
            newNode.next = self.tail
        else:
            newNode.next = node.next
            newNode.prev = node
            node.next = newNode

    def add_in_head(self, newNode):
        self.head.next.prev = newNode
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head

    def clean(self):
        node = self.head.next
        while node.value:
            self.head.next = self.head.next.next
            node = node.next
        self.tail.prev = None

    def len(self):
        node = self.head.next
        result = []
        while node.value:
            result.append(node)
            node = node.next
        return len(result)
