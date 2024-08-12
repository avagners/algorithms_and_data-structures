"""
Реализация №1 алгоритма Питерсона.

По мотивам из книги "Операционные системы. Основы и принципы" Х. Дейтел.
Глава 5 "Асинхронное параллельное программирование".

Алгоритм Питерсона предназначен для работы с двумя потоками. Он является
простым и эффективным решением для обеспечения взаимного исключения.
Редко используется на практике в современных многопоточных системах. Однако
он остаётся важным учебным примером для понимания основ взаимного исключения
и синхронизации.
"""
from threading import Thread
import time

FAVORED_THREAD: int = -1
T1_WANTS_TO_ENTER: bool = False
T2_WANTS_TO_ENTER: bool = False


def thread_1():

    global FAVORED_THREAD, T1_WANTS_TO_ENTER, T2_WANTS_TO_ENTER

    while True:

        T1_WANTS_TO_ENTER = True
        FAVORED_THREAD = 2

        while (T2_WANTS_TO_ENTER and FAVORED_THREAD == 2):
            continue

        for i in range(10):
            print("Thread 1: cs =", i)
            time.sleep(0.5)

        T1_WANTS_TO_ENTER = False


def thread_2():

    global FAVORED_THREAD, T1_WANTS_TO_ENTER, T2_WANTS_TO_ENTER

    while True:

        T2_WANTS_TO_ENTER = True
        FAVORED_THREAD = 1

        while (T1_WANTS_TO_ENTER and FAVORED_THREAD == 1):
            continue

        for i in range(10):
            print("Thread 2: cs =", i)
            time.sleep(0.5)

        T2_WANTS_TO_ENTER = False


if __name__ == "__main__":
    t1 = Thread(target=thread_1)
    t2 = Thread(target=thread_2)
    t1.start()
    t2.start()
