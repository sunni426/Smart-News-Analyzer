'''

general threads wrapper

'''


import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config
import sqlite3
import queue
import threading
import time

# callback: print completion in uploader/nlp/news_analyzer modules
class threads_news(threading.Thread):
    def __init__(self, q, func, func_args, callback, callback_args, *args, **kwargs):
        self.func = func
        self.func_args = func_args
        super().__init__(*args, **kwargs)
    def run(self):
        while True:
            try:
                work = q.get(timeout=5)
            except queue.Empty:
                print('Queue is empty')
                return
            self.func(self.func_args)
            q.task_done()

q = queue.Queue()
for thread in MAX_THREADS:
    q.put_nowait(thread) # put thread ino queue
for _ in range(MAX_THREADS):
    threads_news(q, func, func_args)