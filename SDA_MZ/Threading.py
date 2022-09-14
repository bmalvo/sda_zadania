""" There are a threads tasks solutions """
import random
from threading import Thread, Lock, Event
import time
from concurrent.futures import ThreadPoolExecutor
import datetime

# Task 1


# class MyThread(threading.Thread):
#     """ Class inherits by the Thread
#      class and changes run function
#      for certain purposes"""
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         """Display five random numbers"""
#         for i in range(5):
#             print(random.randint(10, 101))
#             time.sleep(1)


# one_thread = MyThread()
# one_thread.start()

# Task 2


# def give_five_numbers(ide, first, last):
#     time.sleep(random.randint(1, 11))
#     print(datetime.datetime.now(), ide)
#     for i in range(5):
#         print(f'{random.randint(first, last)} by thread - {ide}', end='\n')
#         time.sleep(1)
#
#
# second_thread = threading.Thread(target=give_five_numbers(1, 10, 101))

# Task 3

# with ThreadPoolExecutor() as executor:
#     thread_1 = executor.submit(give_five_numbers, 1, 10, 100)
#     thread_2 = executor.submit(give_five_numbers, 2, 10, 100)
#     thread_3 = executor.submit(give_five_numbers, 3, 10, 100)
#     thread_4 = executor.submit(give_five_numbers, 4, 10, 100)
#     thread_5 = executor.submit(give_five_numbers, 5, 10, 100)
#
#     print(thread_1.result())
#     print(thread_2.result())
#     print(thread_3.result())
#     print(thread_4.result())
#     print(thread_5.result())

# Task 4

name = ''
data_lock = Lock()  # zabezpiecza przed jednoczesnym dostepem do zmiennych
finish_event = Event()


def write_name_loop():
    global finish_event
    global data_lock
    global name
    while True:
        try:
            in_value = input('Write name: \n')
            if in_value == 'exit':
                finish_event.set()
                break
            with data_lock:
                name = in_value
                print(f'Thread [write_name_loop] =>'
                      f' Write new name is: {name}')
        except KeyboardInterrupt:
            finish_event.set()
            break


def check_name_loop():
    global finish_event
    global data_lock
    global name
    old_name = ''
    while True:
        if finish_event.is_set():
            break
        data_lock.acquire()
        try:
            # print(f'checking name, new: {name}, old: {old_name}')
            if old_name != name:
                print(f'Thread [check_name_loop] => old name'
                      f' {old_name}, new name: {name}')
                old_name = name
        finally:
            data_lock.release()
        time.sleep(1)


def threading_ex4():
    writing_thread = Thread(target=write_name_loop)
    reading_thread = Thread(target=check_name_loop)
    writing_thread.start()
    reading_thread.start()
    writing_thread.join()
    reading_thread.join()


write_name_loop()
check_name_loop()
threading_ex4()
