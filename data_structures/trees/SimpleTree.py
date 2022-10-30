from typing import List


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        NewChild.Parent = ParentNode
        if ParentNode is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        '''
        Метод удаления узла вместе с дочерними узлами.
        '''
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def __get_all_nodes(self, node: SimpleTreeNode) -> List[SimpleTreeNode]:
        '''
        Приватный метод рекурсивно проходит по дереву и
        возвращает список всех узлов.
        '''
        nodes = []
        children = node.Children
        nodes.append(node)
        for child in children:
            nodes += self.__get_all_nodes(child)
        return nodes

    def GetAllNodes(self) -> List[SimpleTreeNode]:
        if self.Root is None:
            return []
        return self.__get_all_nodes(self.Root)

    def FindNodesByValue(self, val: int) -> List[SimpleTreeNode]:
        return [node for node in self.GetAllNodes() if node.NodeValue == val]

    def MoveNode(self, OriginalNode, NewParent):
        '''
        Метод перемещения узла вместе с его поддеревом
        в качестве дочернего для узла NewParent.
        '''
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:
        return len(self.GetAllNodes())

    def LeafCount(self) -> int:
        return len([node for node in self.GetAllNodes() if not node.Children])
