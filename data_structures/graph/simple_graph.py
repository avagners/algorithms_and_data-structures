from typing import List


class Vertex:

    def __init__(self, val: int):
        self.Value: int = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: list = [[0] * size for _ in range(size)]
        self.vertex: list = [None] * size

    def AddVertex(self, v: int) -> None:
        # добавление новой вершины
        # с значением value
        # в свободное место массива vertex
        if None not in self.vertex:
            return
        index = self.vertex.index(None)
        self.vertex[index] = Vertex(v)

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v: int) -> None:
        # удаление вершины со всеми её рёбрами
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0
            self.m_adjacency[v][i] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> List[Vertex]:
        # получение списка узлов -- путь из VFrom в VTo
        # поиск в глубину
        assert VTo < self.max_vertex, 'Индекс должен быть меньше кол-ва вершин'
        for vertex in self.vertex:
            vertex.Hit = False
        stack = [self.vertex[VFrom]]
        return self.__find_path(VFrom, VTo, stack)

    def __find_path(self, current_index: int, target_index: int,
                    stack: List[Vertex]):
        self.vertex[current_index].Hit = True
        # если есть ребро между текущей вершиной и целевой,
        # то добавляем в стек целевую вершину и возвращаем стек
        if self.m_adjacency[current_index][target_index] == 1:
            stack.append(self.vertex[target_index])
            return stack
        # проходим циклом по рёбрам текущей вершины
        for index, is_edge in enumerate(self.m_adjacency[current_index]):
            # если вершина смежная (т.е. есть связь) и её еще не рассматривали,
            # то добавляем в стек и проверяем данную вершину
            if is_edge == 1 and not self.vertex[index].Hit:
                stack.append(self.vertex[index])
                return self.__find_path(index, target_index, stack)
        # если непосещенных смежных вершин не осталось,
        # то удаляем из стека верхний элемент
        stack.pop()
        if not stack:
            return []
        # перепроверяем элементы стека на наличие
        # непосещенных смежных вершин
        current_index = self.vertex.index(stack[-1])
        return self.__find_path(current_index, target_index, stack)

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> List[Vertex]:
        # получение списка узлов -- путь из VFrom в VTo
        # поиск в ширину
        for vertex in self.vertex:
            vertex.Hit = False
        queue = [(VFrom, [self.vertex[VFrom]])]
        while queue:
            current_index, path = queue.pop(0)
            current_vertex = self.vertex[current_index]
            current_vertex.Hit = True  # помечаем вершуну как посещенную
            # проверяем все смежные непосещенные вершины
            for check_index in self.__get_adjacent_vertices(current_index):
                if check_index == VTo:
                    path.append(self.vertex[check_index])
                    return path
                queue.append((check_index, path + [self.vertex[check_index]]))
        return []

    def __get_adjacent_vertices(self, index) -> List[int]:
        # метод возвращает смежные вершины, которые еще не посещали
        return [i for i, is_edge in enumerate(self.m_adjacency[index])
                if (is_edge == 1 and not self.vertex[i].Hit)]
