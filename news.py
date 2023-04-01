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

# fileID should be stored internally
class NewsFile(NLPFile):
    def __init__(self, name):
        self.fileID = 0 # will be assigned
        self.name = name
        self.keywords = [] # or some sort of struct? 

    def getKeywords(self):
        # return keywords from this file
        return self.keywords
    
    def searchGov(self):
        # search for relevant keywords in government opendata
        search_results = []

        search_fail = True

        if(search_fail):
            raise ValueError("Search Gov Fail")
        else:
            return 0;

    def searchWiki(self):
        # search for relevant keywords in Wiki
        search_results = []

        search_fail = True

        if(search_fail):
            raise ValueError("Search Wiki Fail")
        else:
            return 0;

    def searchMedia(self):
        # search for relevant keywords in media (e.g. NYT)
        search_results = []

        search_fail = True

        if(search_fail):
            raise ValueError("Search Media Fail")
        else:
            return 0;

    def findDefinitions(self):
        # find definitions of keywords using open services (OpenAI)
        definition_results = []

        find_fail = True

        if(find_fail):
            raise ValueError("Find Definitions Fail")
        else:
            return 0;

    def findContent(self):
        # discover content from the WEB
        content_finds = []

        find_fail = True

        if(find_fail):
            raise ValueError("Find Content Fail")
        else:
            return 0;