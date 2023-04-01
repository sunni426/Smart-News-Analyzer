'''

news feed ingester

'''
from threads_wrapper import News_Thread
from nlp import NLPFile
import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config
import sqlite3
import queue
import threading
import time
import concurrent.futures

# fileID should be stored internally
class NewsFile(NLPFile):
    def __init__(self, name):
        self.fileID = 0 # will be assigned
        self.name = name
        self.keywords = [] # or some sort of struct? 

    def getKeywords(self, queue):
        # return keywords from this file
        return self.keywords
    
    def searchGov(self, queue):
        # search for relevant keywords in government opendata
        search_results = []

        search_fail = True

        if(search_fail):
            raise ValueError("Search Gov Fail")
        else:
            return 0;

    def searchWiki(self, queue):
        # search for relevant keywords in Wiki
        search_results = []

        search_fail = True

        if(search_fail):
            raise ValueError("Search Wiki Fail")
        else:
            return 0;

    def searchMedia(self, queue):
        # search for relevant keywords in media (e.g. NYT)
        search_results = []

        search_fail = True

        if(search_fail):
            raise ValueError("Search Media Fail")
        else:
            return 0;

    def findDefinitions(self, queue):
        # find definitions of keywords using open services (OpenAI)
        definition_results = []

        find_fail = True

        if(find_fail):
            raise ValueError("Find Definitions Fail")
        else:
            return 0;

    def findContent(self, queue):
        # discover content from the WEB
        content_finds = []

        find_fail = True

        if(find_fail):
            raise ValueError("Find Content Fail")
        else:
            return 0;


def callback_news(function_name, queue):
    print(function_name, " finish")


def main():
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
        datefmt="%H:%M:%S")

    news_queue = queue.Queue(maxsize=20)
    running = 1 # first thread
    news_queue.put_nowait(running) # put thread into queue
    news_file = NewsFile("file1.txt")
    News_Thread(news_queue, news_file.getKeyords(), callback=callback_news, callback_args=getKeyords.__name__) # the start()
    news_queue.join() # blocks until queue is empty
    
    # add second thread
    running += 1
    news_queue.put_nowait(running) # put thread into queue
    news_file = NewsFile("file2.txt")
    News_Thread(news_queue, news_file.searchWiki(), callback=callback_news, callback_args=searchWiki.__name__) # the start()
    news_queue.join() # blocks until queue is empty


    # # if want to generate multiple threads for NLP analysis, can use this for loop
    # for _ in range(MAX_THREADS):
    #     News_Thread(news_queue, analyzeSyntax, func_args)
    


if __name__ == "__main__":
    main()