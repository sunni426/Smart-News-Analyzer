'''

general threads wrapper

'''


import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config
import sqlite3


class threads_news(func, func_args, callback_args, kwargs):
    def __init__(self, func, func_args, callback_args):
        # self.fileID = 0 # will be assigned
        # self.filename = filename
        # self.syntax = [] # or some sort of struct? 
        # self.semantics = []
        # self.sentiment = []
        # self.keywords = []
        # File.__init__(self,filename)