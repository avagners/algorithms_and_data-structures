"""
Реализация №2 алгоритма Питерсона.

По мотивам из книги "Операционные системы. Основы и принципы" Х. Дейтел.
Глава 5 "Асинхронное параллельное программирование".

Алгоритм Питерсона предназначен для работы с двумя потоками. Он является
простым и эффективным решением для обеспечения взаимного исключения.
Редко используется на практике в современных многопоточных системах. Однако
он остаётся важным учебным примером для понимания основ взаимного исключения
и синхронизации.
"""
import time
from threading import Thread, get_ident
from typing import List
import random


class PetersonLock:
    def __init__(self):
        self.flag: List[bool, bool] = [False, False]
        self.favored_thread: int = 0

    def lock(self, thread_id):
        other_thread = 1 - thread_id
        self.flag[thread_id] = True
        self.favored_thread = thread_id

        # цикл активного ожидания
        while self.flag[other_thread] and self.favored_thread == thread_id:
            pass

    def unlock(self, thread_id):
        self.flag[thread_id] = False


class Buffer:
    def __init__(self) -> None:
        self.buffer: List[int] = []

    def set(self, number: int):
        self.buffer.append(number)

    def get(self):
        return self.buffer.pop(0)


class Producer(Thread):
    def __init__(self, buffer: Buffer, lock: PetersonLock) -> None:
        super().__init__()
        self.shared_location = buffer
        self.lock = lock

    def run(self):
        for i in range(1, 5):
            self.lock.lock(0)  # здесь используем индекс потока в качестве идентификатора
            try:
                time.sleep(random.randint(1, 5))
                self.shared_location.set(i)
                print(f"Поток {get_ident()} записал в буфер значение: {i}")
            except BaseException as e:
                print(e)
            self.lock.unlock(0)
        print("Producer завершил генерирование сообщений")


class Consumer(Thread):
    def __init__(self, buffer: Buffer, lock: PetersonLock) -> None:
        super().__init__()
        self.shared_location = buffer
        self.lock = lock

    def run(self):
        summa: int = 0
        for _ in range(4):
            self.lock.lock(1)  # здесь используем индекс потока в качестве идентификатора
            try:
                time.sleep(random.randint(1, 5))
                number = self.shared_location.get()
                print(f"Поток {get_ident()} прочитал из буфера значение: {number}")
                summa += number
            except BaseException as e:
                print(e)
            self.lock.unlock(1)
        print(f"Сумма прочитанных сообщений: {summa}")


if __name__ == "__main__":
    lock = PetersonLock()
    buffer = Buffer()

    producer = Producer(buffer, lock)
    consumer = Consumer(buffer, lock)

    producer.start()
    consumer.start()
