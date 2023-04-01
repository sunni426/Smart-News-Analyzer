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
import uploader
import nlp
import news
import concurrent.futures

# callback: print completion in uploader/nlp/news_analyzer modules
class News_Thread(threading.Thread):
    def __init__(self, queue_in, func, func_args, callback, callback_args, *args, **kwargs):
        self.func = func
        self.func_args = func_args
        super().__init__(*args, **kwargs)
    def run(self):
        while True:
            try:
                work = queue_in.get(timeout=5)
            except queue_in.empty:
                print('Queue is empty')
                return
            name = func.__name__
            logging.debug("running %d from queue", name)
            self.func(self.func_args)
            if(queue_in.task_done()): # Indicate that a formerly enqueued task is complete
                callback(callback_args)
            

# callback: a function passed as an argument to another function, which is expected to
# call this callback function in its definition 


def main():
    pass

if __name__ == "__main__":
    main()



# some code extracted from here: https://stackoverflow.com/questions/35160417/threading-queue-working-example
