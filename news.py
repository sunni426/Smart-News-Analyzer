'''

news feed ingester

used the 'feedparser' library, which can parse RSS and Atom feeds

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
import feedparser

# fileID should be stored internally
class NewsFile(NLPFile):
    def __init__(self, name):
        self.fileID = 0 # will be assigned
        self.name = name
        self.keywords = [] # or some sort of struct? 


def ingest_feed(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        # get title, summary, and link for each entry
        title = entry.title
        summary = entry.summary
        link = entry.link

        print(f'title: {title}')
        print(f'summary: {summary}')
        print(f'link: {link}')



def getKeywords(file):
    # return keywords from this file
    logging.info("getKeywords executing")
    return file.keywords


def callback_news(function_name):
    # print(function_name, " finish")
    logger.info("%s finish, in callback", function_name)


def main():

    # Example usage: ingest the XML feed from NASA: International Space Station Report
    url = 'https://blogs.nasa.gov/stationreport/feed/'
    ingest_feed(url)
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
        datefmt="%H:%M:%S")

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