'''

nlp analysis

'''
from threads_wrapper import News_Thread
from uploader import *
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
import nltk
from textblob import TextBlob
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import json
# import gensim
# from gensim.summarization import summarize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

MAX_THREADS = 5

def summarize(contents):
    # Tokenize the text into sentences
    sentences = sent_tokenize(contents)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentences = [sentence for sentence in sentences if not any(word.lower() in stop_words for word in sentence.split())]

    # Get the frequency distribution of words
    words = nltk.word_tokenize(' '.join(filtered_sentences))
    fdist = FreqDist(words)

    # Get the most common words
    top_words = [word for word, _ in fdist.most_common(5)]

    # Generate the summary
    summary_sentences = []
    for sentence in filtered_sentences:
        if any(word.lower() in top_words for word in sentence.split()):
            summary_sentences.append(sentence)
    summary = ' '.join(summary_sentences)



def analyze(file):

    keywords_syntax = []

    # implicitly creating users.db if not in cwd 
    news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
    news_cur = news_con.cursor() # to execute SQL statements, need DB cursor

    # get contents of file
    contents = file.contents

    # tokenize contents
    sentences = nltk.sent_tokenize(contents)
    paragraphs = contents.split('\n')

    ############################ ANALYZE SYNTAX ############################
    # get number of sentences, paragraphs, words
    words = nltk.word_tokenize(contents)
    word_count = len(words)
    sentence_count = len(sentences)
    paragraph_count = len(paragraphs)
    blob_all = TextBlob(contents)
    keywords_all = blob_all.noun_phrases
    keywords_top3 = [keyword for keyword, count in Counter(keywords_all).most_common(3)]
    print(f'file.fileID: {file.fileID}')
    print(f'paragraph_count: {paragraph_count}')
    print(f'word_count: {word_count}')
    print(f'date.today(): {date.today()}')
    print(f'keywords_top3: {keywords_top3}')

    insert_data = [file.fileID, paragraph_count, word_count, date.today(), json.dumps(keywords_top3)]

    # insert syntax analysis into DB
    try:
        news_cur.execute("INSERT or IGNORE INTO syntax VALUES (?, ?, ?, ?, ?)", insert_data)
        news_con.commit()
    except news_con.Error:
        news_con.rollback()
        raise ValueError("user DB insertion error")

    # queues & threading setup
    message = "keyword 1 is " + keywords_top3[0]
    logger.info("analyzeSyntax executing, : %s", message)
    logger.info("analyzeSyntax received event. Exiting")


    ############################ ANALYZE SEMANTICS ############################
    keywords_semantics = []
    summaries = []
    labels = []

    for para_no, paragraph in enumerate(paragraphs):
        blob = TextBlob(paragraph)
        keywords_para = blob.noun_phrases
        keywords_para_top5 = [keyword for keyword, count in Counter(keywords_para).most_common(5)]
        if(blob.sentences):
            summary = blob.sentences[0].replace('\n', '')
        else:
            summary = []
        print(f'keywords_para: {keywords_para_top5}')
        print(f'summary: {summary}')
        print(f'para_no: {para_no}')
        insert_data = [file.fileID, para_no, str(summary), json.dumps(keywords_para_top5)]

        # insert syntax analysis into DB
        try:
            news_cur.execute("INSERT or IGNORE INTO semantic VALUES (?, ?, ?, ?)", insert_data)
            news_con.commit()
        except news_con.Error:
            # Rolling back in case of error
            # print('user db insertion error')
            news_con.rollback()
            raise ValueError("user DB insertion error")

    # queues & threading setup
    message = "keyword 1 is " + "word" # keywords_para_top5[0]
    logger.info("analyzeSemantics executing, : %s", message)
    logger.info("analyzeSemantics received event. Exiting")


    ############################ ANALYZE SENTIMENT ############################
    # sentiment analysis

    for para_no, paragraph in enumerate(paragraphs):
        blob = TextBlob(paragraph)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiments = ('positive')
        elif sentiment < 0:
            sentiments = ('negative')
        else:
            sentiments = ('neutral')

        insert_data = [file.fileID, para_no, sentiments]

        # insert syntax analysis into DB
        try:
            news_cur.execute("INSERT or IGNORE INTO sentiment VALUES (?, ?, ?)", insert_data)
            news_con.commit()
        except news_con.Error:
            news_con.rollback()
            raise ValueError("user DB insertion error")

    # queues & threading setup
    message = sentiment
    logger.info("analyzeSentiment executing, sentiment is : %s", message)
    logger.info("analyzeSentiment received event. Exiting")

    news_con.close()



def callback_nlp(function_name):
    # print(function_name, " finish")
    logger.info("%s finish, in callback", function_name)


def main():

    logger.debug('In NLP main')
    
    user7 = User("user7")
    filename = "text.txt"
    file, contents = user7.uploadFile(filename)
    user7.storeFile(filename)
    analyze(file)

    # # news_queue = queue.Queue(maxsize=20) # kind of like a pipeline
    # # event = threading.Event() # this is more used with ThreadPoolExecutor
    # running = 1 # first thread
    # file1 = File("file1.txt")
    # thread1 = News_Thread(func=analyzeSyntax, func_args=file1, callback=callback_nlp, callback_args=analyzeSyntax.__name__)
    # news_queue.put_nowait(thread1) # put thread ino queue
    # thread1.run()
    # news_queue.join() # blocks until queue is empty

    # # if want to generate multiple threads for NLP analysis, can use this for loop
    # for _ in range(MAX_THREADS):
    #     News_Thread(news_queue, analyzeSyntax, func_args)
    


if __name__ == "__main__":
    logger.debug('In NLP main')
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