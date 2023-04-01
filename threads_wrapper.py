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
from uploader import *
# import nlp
# import news
import concurrent.futures

# callback: print completion in uploader/nlp/news_analyzer modules
class News_Thread(threading.Thread):
    def __init__(self, func, func_args, callback, callback_args, *args, **kwargs):
        self.func = func
        self.func_args = func_args
        self.callback = callback
        self.callback_args = callback_args
        logger.info("%s thread init", func_args)
        super().__init__(*args, **kwargs)
    def run(self):
        # while True:
        # if news_queue.empty:
        #     print('Queue is empty')
        #     logger.info("Queue is empty")
        #     return
        # else:
            # work = news_queue.get(timeout=2)
        logger.info("running %s from queue", self.func_args)
        self.func(self.func_args)
        # if(news_queue.task_done()): # Indicate that a formerly enqueued task is complete
        self.callback(self.callback_args)
        if news_queue.empty:
            exit()
            

# callback: a function passed as an argument to another function, which is expected to
# call this callback function in its definition 


def main():
    pass

if __name__ == "__main__":
    main()



# some code extracted from here: https://stackoverflow.com/questions/35160417/threading-queue-working-example
