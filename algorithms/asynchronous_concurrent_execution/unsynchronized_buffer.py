"""
По мотивам из книги "Операционные системы. Основы и принципы" Х. Дейтел.
Глава 5 "Асинхронное параллельное программирование".

Данный пример доказывает, что доступ к разделяемым объектам со стороны
параллельных потоков должен контролироваться очень тщательно, иначе
программа будет выдавать некорректные результаты.

Каждый запуск данного кода будет выдавать непредсказуемый результат.
"""
import time
import random
from threading import Thread


class Buffer:
    def __init__(self) -> None:
        self.buffer: set = set()

    def set(self, number: int):
        self.buffer.add(number)

    def get(self):
        return self.buffer.pop()


class Producer(Thread):
    def __init__(self, buffer: Buffer) -> None:
        super().__init__()
        self.shared_location = buffer

    def run(self):
        for i in range(1, 5):
            try:
                time.sleep(random.randint(1, 5))
                self.shared_location.set(i)
                print(f"Поток {self.ident} записал в буфер значение: {i}")
            except BaseException as e:
                print(e)
        print("Producer завершил генерирование сообщений")


class Consumer(Thread):
    def __init__(self, buffer: Buffer) -> None:
        super().__init__()
        self.shared_location = buffer

    def run(self):
        summa: int = 0
        for _ in range(4):
            try:
                time.sleep(random.randint(1, 5))
                number = self.shared_location.get()
                print(f"Поток {self.ident} считывает из буфера значение: {number}")
                summa += number
            except BaseException as e:
                print(e)
        print(f"Сумма прочитанных сообщений: {summa}")


if __name__ == "__main__":
    buffer = Buffer()
    producer = Producer(buffer)
    concumer = Consumer(buffer)

    producer.start()
    concumer.start()
