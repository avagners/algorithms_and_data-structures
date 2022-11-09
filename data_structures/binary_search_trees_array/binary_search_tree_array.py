class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2**(depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def __find_index(self, key, index):
        if index > len(self.Tree):
            return None
        if not self.Tree[index]:
            return -index
        if self.Tree[index] == key:
            return index
        if self.Tree[index] > key:
            index_left_child = 2 * index + 1
            return self.__find_index(key, index_left_child)
        if self.Tree[index] < key:
            index_rignt_child = 2 * index + 2
            return self.__find_index(key, index_rignt_child)

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        return self.__find_index(key, 0)

    def AddKey(self, key):
        # добавляем ключ в массив
        return -1
        # индекс добавленного/существующего ключа или -1 если не удалось
