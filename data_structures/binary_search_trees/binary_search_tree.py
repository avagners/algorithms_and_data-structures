class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node: BSTNode = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey: bool = False  # True если узел найден
        self.ToLeft: bool = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node: BSTNode):
        self.Root = node  # корень дерева, или None
        self.__size = 0 if not node else 1

    def __find_node(self, search_result: BSTFind, key: int) -> BSTNode:
        node = search_result.Node
        if key == node.NodeKey:
            search_result.NodeHasKey = True
            return search_result
        elif key < node.NodeKey and node.LeftChild:
            search_result.Node = node.LeftChild
            return self.__find_node(search_result, key)
        elif key > node.NodeKey and node.RightChild:
            search_result.Node = node.RightChild
            return self.__find_node(search_result, key)
        search_result.ToLeft = True if key < node.NodeKey else False
        return search_result

    def FindNodeByKey(self, key: int) -> BSTFind:
        if not self.Root:
            return BSTFind()
        search_result = BSTFind()
        search_result.Node = self.Root
        return self.__find_node(search_result, key)

    def AddKeyValue(self, key: int, val: int):
        search_result = self.FindNodeByKey(key)
        if search_result.NodeHasKey:
            return False  # если ключ уже есть
        new_node = BSTNode(key, val, parent=search_result.Node)
        if not search_result.Node:
            self.Root = BSTNode(key, val, parent=None)
        elif search_result.ToLeft:
            search_result.Node.LeftChild = new_node
        else:
            search_result.Node.RightChild = new_node
        self.__size += 1

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if not self.Root:
            return None
        if FindMax and FromNode.RightChild:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        if not FindMax and FromNode.LeftChild:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        return FromNode

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self) -> int:
        return self.__size  # количество узлов в дереве
