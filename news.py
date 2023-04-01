'''

news feed ingester

'''
from uploader import *
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

def getKeywords(file):
    # return keywords from this file
    logging.info("getKeywords executing")
    return file.keywords

def searchGov(file):
    # search for relevant keywords in government opendata
    search_results = []

    search_fail = True

    logging.info("searchGov executing")

    if(search_fail):
        raise ValueError("Search Gov Fail")
    else:
        return 0;

def searchWiki(file):
    # search for relevant keywords in Wiki
    search_results = []

    search_fail = True

    logging.info("searchWiki executing")

    if(search_fail):
        raise ValueError("Search Wiki Fail")
    else:
        return 0;

def searchMedia(file):
    # search for relevant keywords in media (e.g. NYT)
    search_results = []

    search_fail = True

    logging.info("searchMedia executing")

    if(search_fail):
        raise ValueError("Search Media Fail")
    else:
        return 0;

def findDefinitions(file):
    # find definitions of keywords using open services (OpenAI)
    definition_results = []

    find_fail = True

    logging.info("findDefinitions executing")

    if(find_fail):
        raise ValueError("Find Definitions Fail")
    else:
        return 0;

def findContent(file):
    # discover content from the WEB
    content_finds = []

    find_fail = True

    logging.info("findContent executing")

    if(find_fail):
        raise ValueError("Find Content Fail")
    else:
        return 0;


def callback_news(function_name):
    # print(function_name, " finish")
    logger.info("%s finish, in callback", function_name)


def main():
    
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #     datefmt="%H:%M:%S")

    logger.debug('In news main')

    news_queue = queue.Queue(maxsize=20)
    running = 1 # first thread
    news_file2 = NewsFile("file2.txt")
    thread2 = News_Thread(func=getKeywords, func_args=news_file2, callback=callback_news, callback_args=getKeywords.__name__) # the start()
    news_queue.put_nowait(thread2) # put thread into queue
    thread2.run()
    news_queue.join() # blocks program termination until queue is empty
    
    # add second thread
    running += 1
    news_queue.put_nowait(running) # put thread into queue
    news_file3 = NewsFile("file3.txt")
    thread3 = News_Thread(func=searchWiki, func_args=news_file3, callback=callback_news, callback_args=searchWiki.__name__) # the start()
    news_queue.put_nowait(thread2) # put thread into queue
    thread3.run()
    news_queue.join() # blocks until queue is empty


    # # if want to generate multiple threads for NLP analysis, can use this for loop
    # for _ in range(MAX_THREADS):
    #     News_Thread(news_queue, analyzeSyntax, func_args)
    


if __name__ == "__main__":
    main()