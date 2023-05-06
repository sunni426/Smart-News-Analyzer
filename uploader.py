'''

secure file uploader/ingester

'''

import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config
import os
import os.path as path # https://docs.python.org/3/library/os.path.html
import sqlite3
import queue
import threading
import time
import login
from datetime import date
import json
# from news import ingest_feed

# import db_init # to initialize database (rewrite, must delete prev)

# queue shared by all modules
news_queue = queue.Queue(maxsize=20) # kind of like a pipeline


# creating a logger object
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
# creating a FileHandler that writes to a file
file_handler = logging.FileHandler('logger.log')
file_handler.setLevel(logging.DEBUG)
# creating a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# adding the FileHandler to the logger
logger.addHandler(file_handler)

MAX_USERS = 1000 # max number users the system can support. can change values
MAX_FILES = 10 # max number files each user can have. can change values
userid = 1
userid_list = []
fileid = 1
fileid_list = []


# Entity associated with user; Database initiliaizing associated with User
class User:
    def __init__(self, name):
        
        # implicitly creating users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
        global userid 

        self.numfiles = 0
        self.fileIDs = []
        # serialize list into string
        fileIDs_store = json.dumps(self.fileIDs)

        if userid < MAX_USERS:
            self.userID = userid
            
            # To change the value of a global variable inside a function, refer to the variable by using the global keyword
            userid += 1
            self.name = name
            insert_data = [self.userID, self.name, self.numfiles, fileIDs_store]

            userid_list.append(userid)
            
            try:
                news_cur.execute("INSERT OR IGNORE INTO user VALUES (?, ?, ?, ?)", insert_data)
                news_con.commit()
            except news_con.Error:
                # Rolling back in case of error
                print('user db insertion error')
                news_con.rollback()
                raise ValueError("user DB insertion error")
        else:
            raise ValueError("Maximum number of users, storage full")

        news_con.close()

        
    # User login module using Gmail authentication
    def user_login(self):
       login.main()
    

    def viewFiles(self):
        pass

    # Upload file contents from local directory: create a File object. Assigns fileID and userID
    def uploadFile(self, filename):
    
        userpath = os.path.abspath(filename)

        try:
            with open(userpath, "r") as file:
                contents = file.read()
                fileID = self.numfiles + 1
                if fileid > MAX_FILES:
                    raise ValueError("Maximum number of files, storage full")
                self.numfiles = self.numfiles + 1
                # initialize file object to store in database
                file = File(filename, fileID, self.userID, userpath, date.today(), contents)

                return file, contents

        except FileNotFoundError:
            raise ValueError("File does not exist")
        except:
            raise ValueError("Upload fail")


    # Store file into database
    def storeFile(self, filename):

        try:

            file, contents = self.uploadFile(filename)

            # Create connection to db; implicitly creates users.db if not in cwd 
            news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
            news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
            global fileid 
        
            # insert file contents into database
            insert_data = [file.fileID, file.userID, file.filename, file.fileformat, file.filepath, file.lastmodified, file.contents]

            fileid_list.append(fileid)
            
            try:

                # Create new entry in DB to store this file
                news_cur.execute("INSERT OR IGNORE INTO file VALUES (?, ?, ?, ?, ?, ?, ?)", insert_data)

                # Update user table: increase number of files associated with user by 1
                news_cur.execute("UPDATE user SET numfiles=? WHERE userID=?", (self.numfiles,self.userID,))

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
                news_cur.execute("UPDATE user SET fileIDs=? WHERE userID=?",(file_list,self.userID,))
                news_con.commit()

            except news_con.Error:
                news_con.rollback()
                raise ValueError("file DB insertion error")

            news_con.close()

        except Exception as e:
            raise ValueError("Error storing file contents:", e)



class File:
    def __init__(self, filename, fileID, userID, filepath, lastmodified, contents):
        self.fileID = fileID
        self.userID = userID
        self.filename = filename
        self.fileformat = 'txt'
        self.filepath = filepath
        self.lastmodified = lastmodified
        self.contents = contents


    def getAccount(self):
        pass



def main():

    user6 = User("Name6")
    user6.storeFile("example1.txt")
    user6.storeFile("example.txt")
    user6.storeFile("example2.txt")
    user6.storeFile("requirements.txt")
    
    # url = 'https://blogs.nasa.gov/stationreport/feed/'
    # user6.user_ingest_feed(url)


if __name__ == "__main__":
    # logger.info('In uploader main') # check logger functionality
    main()
