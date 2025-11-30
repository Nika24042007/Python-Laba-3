

class Queue:
    """
    Класс для работы с очередью на list
    """
    def __init__(self):
        """
        Создание очереди
        """
        self.queue = []

    def enqueue(self, x: int) -> None:
        """
        Добавления элемента в очередь
        :param x: элемент, который нужно добавить
        """
        self.queue.append(x)


    def front(self) -> int:
        """
        Простер первого элемента в очереди
        
        :return: первый элемент очереди
        """
        if not self.is_empty():
            return self.queue[0]
        else:
            None

    def is_empty(self) -> bool:
        """
        Проверка очереди на пустоту
        
        :return: пустой ли сиписок или нет
        """
        return len(self.queue) == 0

    def dequeue(self) -> int:
        """
        Удаление первого элемента очереди
        :return: удаленный элемент
        """
        if not self.is_empty():
            x = self.queue.pop(0)
            return x
        else:
            None
    def __len__(self) -> int:
        """
        Определение длины очереди
        :return: количество элементов в очереди
        """
        return len(self.queue)
        
