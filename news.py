'''

news feed ingester

used the 'feedparser' library, which can parse RSS and Atom feeds

'''

from uploader import *
from threads_wrapper import News_Thread
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
from datetime import date
import feedparser

MAX_THREADS = 10


# input any url; will check if the webpage has a RSS or Atom feed.
def ingest_feed(url):

    html = feedparser.parse(url)

    feed_url = ""

    # look for link to RSS or Atom feed
    link_type = ""
    for link in html.feed.links:
        if link.type == 'application/rss+xml' or link.type == 'application/atom+xml':
            feed_url = link.href
            link_type = link.type
            break

    if feed_url:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            # get title, summary, and link for each entry
            title = entry.title
            summary = entry.summary
            keywords = []

            # print(f'title: {title}')
            # print(f'summary: {summary}')
            # print(f'link: {link}')
            
            return title, summary, link_type

    else:
        raise ValueError("Error, no feed found:")



# store results of feed ingester into database with associated file and userID
# the "contents" column will store the summary of the news article
def storeFeed(url, user):

    try:

        title, summary, link_type = ingest_feed(url)

        # Create connection to db; implicitly creates users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
    
        # insert file contents into database
        user.numfiles = user.numfiles + 1
        print(f'numfiles: {user.numfiles}')
        print(f'userID: {user.userID}')
        file = File(title, user.numfiles, user.userID, url, date.today(), summary)
        
        # fileid_list.append(fileid)
        
        try:

            # Create new entry in DB to store this file
            insert_data = [user.numfiles, user.userID, title, link_type, url, date.today(), summary]
            news_cur.execute("INSERT OR IGNORE INTO file VALUES (?, ?, ?, ?, ?, ?, ?)", insert_data)

            x = news_cur.execute("SELECT userID FROM user").fetchone()[0]

            # Update user table: add in file id
            # retrieve list of files by this user from database
            file_list = news_cur.execute("SELECT fileIDs FROM user").fetchone()[0]

            files = []
            # deserialize list from string
            files = json.loads(file_list)

            # add new fileID to list
            files.append(file.fileID)
            files = list(set(files))

            # serialize updated list to a string
            file_list = json.dumps(files)

            # update entry in database
            news_cur.execute("UPDATE user SET fileIDs=? WHERE userID=?",(file_list,user.userID,))
            news_con.commit()

            return file

        except news_con.Error:
            news_con.rollback()
            raise ValueError("File DB insertion error")

        news_con.close()

    except Exception:
        raise ValueError("Error storing feed ingester contents")



def callback_news(function_name):
    # print(function_name, " finish")
    logger.info("%s finish, in callback", function_name)


def main():

    # Example usage: ingest the XML feed from NASA: International Space Station Report
    user7 = User("user7")
    url = 'https://blogs.nasa.gov/stationreport/feed/'
    # url = 'https://rss.art19.com/apology-line'
    storeFeed(url, user7)

    # logging and multithreading/queue implementation and testing
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
        datefmt="%H:%M:%S")

    logger.debug('In news main')

    # news_queue = queue.Queue(maxsize=20)
    # running = 1 # first thread
    # file1 = storeFeed('https://blogs.nasa.gov/stationreport/feed/', user7)
    # thread2 = News_Thread(func=ingest_feed, func_args=file1, callback=callback_news, callback_args=ingest_feed.__name__) # the start()
    # news_queue.put_nowait(thread2) # put thread into queue
    # thread2.run()
    # news_queue.join() # blocks program termination until queue is empty
    
    # # add second thread
    # running += 1
    # news_queue.put_nowait(running) # put thread into queue
    # file2 = storeFeed('https://rss.art19.com/apology-line', user7)
    # thread3 = News_Thread(func=ingest_feed, func_args=file2, callback=callback_news, callback_args=ingest_feed.__name__) # the start()
    # news_queue.put_nowait(thread3) # put thread into queue
    # thread3.run()
    # news_queue.join() # blocks until queue is empty


    # # if want to generate multiple threads for NLP analysis, can use this for loop
    # for _ in range(MAX_THREADS):
    #     News_Thread(news_queue, analyzeSyntax, func_args)
    



if __name__ == "__main__":
    main()