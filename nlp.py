'''

test nlp analysis

'''
from threads_wrapper import News_Thread
from uploader import File
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

MAX_THREADS = 5

# fileID should be stored internally
class NLPFile(File):
    def __init__(self, filename):
        self.fileID = 0 # will be assigned
        self.filename = filename
        self.syntax = [] # or some sort of struct? 
        self.semantics = []
        self.sentiment = []
        self.keywords = []
        File.__init__(self,filename)

    def getTest(self, fileID):
        # parse uploaded file into text format (a string) of class NLPFile, with new field
        pass
    
    def analyzeSyntax(self, queue):

        # implicitly creating users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
        
        # parsing analysis implementation
        # these fields will be stored in the syntax member of NLPFile after NLP
        keywords_syntax = ['word1','word2','word3']
        # names = []
        # locations = []
        # institutions = []
        # address = []
        paragraph_count = 2
        word_count = 100
        date_created = "March-18-2023"
        summary = "this is the implementation of test nlp of smart doc uploader"
        # line_count = 0

        insert_data = [self.fileID, paragraph_count, word_count, 
                date_created, summary, keywords_syntax[0], keywords_syntax[1], keywords_syntax[2]]

        # insert syntax analysis into DB
        try:
            news_cur.execute("INSERT INTO syntax VALUES (?, ?, ?, ?, ?, ?, ?, ?)", insert_data)
            news_con.commit()
        except news_con.Error:
            # Rolling back in case of error
            # print('user db insertion error')
            news_con.rollback()
            raise ValueError("user DB insertion error")

        syntax_fail = True

        if(syntax_fail):
            raise ValueError("Syntax analysis failed")
        else:
            return 0;

        # queues & threading setup
        message = "keyword 1 is " + keywords_syntax[0]
        logging.info("analyzeSyntax executing, : %s", message)
        queue.put(message)
        logging.info("analyzeSyntax received event. Exiting")

        news_con.close()


    def analyzeSemantics(self, queue, event, para_no):
        # these fields will be stored in the semantics member of NLPFile
        keywords_semantics = []
        summaries = []
        labels = []

        # to put: analysis implementation
        # storing in semantics
        # implicitly creating users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
        
        summaries.append('this text is about analyzing the meaning of this document.')
        keywords_semantics.append('meaning')
        keywords_semantics.append('analysis')
        # print(f'\n\nsummaries[0]: {summaries[0]}\n\n')
        insert_data = [self.fileID, para_no, summaries[para_no], keywords_semantics[0], keywords_semantics[1]]

        # insert syntax analysis into DB
        try:
            news_cur.execute("INSERT INTO semantic VALUES (?, ?, ?, ?, ?)", insert_data)
            news_con.commit()
        except news_con.Error:
            # Rolling back in case of error
            # print('user db insertion error')
            news_con.rollback()
            raise ValueError("user DB insertion error")

        semantics_fail = True

        if(semantics_fail):
            raise ValueError("Semantics analysis failed")
        else:
            return 0;

        # queues & threading setup
        message = "keyword 1 is " + keywords_semantics[0]
        logging.info("analyzeSemantics executing, : %s", message)
        queue.put(message)
        logging.info("analyzeSemantics received event. Exiting")

        news_con.close()


    def analyzeSentiment(self, queue, para_no):

        # sentiment analysis
        # these fields will be stored in the sentiment member of NLPFile
        sentiment = 'positive'

        # to put: analysis implementation
        # storing in sentiment
        # implicitly creating users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
        
        insert_data = [self.fileID, para_no, sentiment]

        # insert syntax analysis into DB
        try:
            news_cur.execute("INSERT INTO sentiment VALUES (?, ?, ?)", insert_data)
            news_con.commit()
        except news_con.Error:
            # Rolling back in case of error
            # print('user db insertion error')
            news_con.rollback()
            raise ValueError("user DB insertion error")

        sentiment_fail = True

        if(sentiment_fail):
            raise ValueError("Sentiment analysis failed")
        else:
            return 0;
        
        # queues & threading setup
        message = sentiment
        logging.info("analyzeSentiment executing, sentiment is : %s", message)
        queue.put(message)
        logging.info("analyzeSentiment received event. Exiting")

        news_con.close()


def callback_nlp(function_name):
    print(function_name, " finish")


def main():

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
        datefmt="%H:%M:%S")

    news_queue = queue.Queue(maxsize=20) # kind of like a pipeline
    # event = threading.Event() # this is more used with ThreadPoolExecutor
    running = 1 # first thread
    news_queue.put_nowait(thread) # put thread ino queue
    file = NLPFile("file1.txt")
    News_Thread(news_queue, file.analyzeSyntax(), callback=callback_nlp, callback_args=analyzeSyntax.__name__)
    news_queue.join() # blocks until queue is empty

    # # if want to generate multiple threads for NLP analysis, can use this for loop
    # for _ in range(MAX_THREADS):
    #     News_Thread(news_queue, analyzeSyntax, func_args)
    


if __name__ == "__main__":
    main()


'''

getText(fileID)
    Returns textID if successful: associated with the file but in the specific text format that this application supports for subsequent NLP analysis
analyzeSyntax(fileID)
Returns syntaxID if successful
    Stores info with fileID, accessible by syntaxID
analyzeSemantics(fileID)
Returns semanticsID if successful
    Stores info with fileID, accessible by semanticsID
analyzeSentiment(fileID)
    Returns sentimentID if successful
Stores info with fileID, accessible by sentimentID
    display(fileID, mode)
    mode: syntax, semantics, or sentiment


def getText(fileID):
    if PDF
    if image


# extract PDF XML format https://towardsdatascience.com/how-to-extract-data-from-pdf-forms-using-python-10b5e5f26f70 
import PyPDF2 as pypdf
def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value=haystack[key]
        except:
            continue
        if key==needle:
            return value
        if isinstance(value,dict):            
            x=findInDict(needle,value)            
            if x is not None:
                return x
pdfobject=open('CTRX_filled.pdf','rb')
pdf=pypdf.PdfFileReader(pdfobject)
xfa=findInDict('/XFA',pdf.resolvedObjects)
xml=xfa[7].getObject().getData()



# Extract Text from Image using Python - Tesseract is an open source OCR (optical character recognition)
    with Two Python libraries:
        pytesseract
        pillow
    https://pyshark.com/extract-text-from-image-using-python/ 


'''