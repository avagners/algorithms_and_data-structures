class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey: int = key  # ключ узла
        self.NodeValue: int = val  # значение в узле
        self.Parent: BSTNode = parent  # родитель или None для корня
        self.LeftChild: BSTNode = None  # левый потомок
        self.RightChild: BSTNode = None  # правый потомок


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

    def __insert_node(self, parent: BSTNode, new_node: BSTNode, is_left):
        if is_left:
            parent.LeftChild = new_node
        else:
            parent.RightChild = new_node

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        bst_find = self.FindNodeByKey(key)
        if not bst_find.NodeHasKey:
            return False
        node_delete = bst_find.Node
        # находим преемника
        node_successor = self.FinMinMax(node_delete.RightChild, False)
        # проверяем правый или левый узел удаляем
        is_left = node_delete.NodeKey < node_delete.Parent.NodeKey
        # если у преемника нет наследников, то удаляем у родителя преемника
        # удаляем левого наследника
        if not node_successor.LeftChild and not node_successor.RightChild:
            node_successor.Parent.LeftChild = None
            self.__insert_node(node_delete.Parent, node_successor, is_left)
        # если у преемника есть только правый наследник, то
        # на место преемника ставим этот наследник
        elif not node_successor.LeftChild:
            node_successor.Parent.LeftChild = node_successor.RightChild
            node_successor.RightChild.Parent = node_successor.Parent
            self.__insert_node(node_delete.Parent, node_successor, is_left)
        # перемещаем преемника на место удаленного узла
        node_successor.Parent = node_delete.Parent
        node_successor.LeftChild = node_delete.LeftChild
        node_successor.RightChild = node_delete.RightChild
        node_successor.RightChild.Parent = node_successor
        node_successor.LeftChild.Parent = node_successor
        self.__size -= 1

    def Count(self) -> int:
        return self.__size  # количество узлов в дереве

    def __get_all_nodes(self, node: BSTNode) -> list:
        '''
        Приватный метод рекурсивно проходит по дереву и
        возвращает список всех узлов.
        '''
        nodes = []
        nodes.append(node)
        if node.LeftChild:
            nodes += self.__get_all_nodes(node.LeftChild)
        if node.RightChild:
            nodes += self.__get_all_nodes(node.RightChild)
        return nodes

    def GetAllNodes(self) -> list:
        if not self.Root:
            return []
        return self.__get_all_nodes(self.Root)
