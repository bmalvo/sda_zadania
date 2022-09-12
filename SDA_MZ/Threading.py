import random
import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(5):
            print(random.randint(10, 101))
            time.sleep(5)


one_thread = MyThread()
one_thread.start()
