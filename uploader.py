'''

secure file uploader/ingester

'''

import numpy as np
import tracemalloc
import cProfile, pstats
import logging
# import logging.config
import os.path as path # https://docs.python.org/3/library/os.path.html
import sqlite3
import queue
import threading
import time
# import db_init # to initialize database (rewrite, must delete prev)


# creating a logger object
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
# creatnig a FileHandler that writes to a file
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


# associated with user
class User:
    def __init__(self, name): # let userID be internal to this func and not as a param, 3/19
        
        # implicitly creating users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
        global userid 

        if userid in userid_list:
            userid += 1
        if userid < MAX_USERS:
            self.userID = userid
            # userid_list.append(userid)
            # To change the value of a global variable inside a function, refer to the variable by using the global keyword
            userid += 1
            self.name = name
            insert_data = [self.userID, self.name]

            userid_list.append(userid)
            
            # print(f'self.userID: {self.userID}, self.name: {self.name}')
            try:
                news_cur.execute("INSERT INTO user VALUES (?, ?)", insert_data)
                news_con.commit()
            except news_con.Error:
                # Rolling back in case of error
                # print('user db insertion error')
                news_con.rollback()
                raise ValueError("user DB insertion error")
        else:
            raise ValueError("Maximum number of users, storage full")

        news_con.close()

        
    def setPassword(self):
        pass
    
    def viewFiles(self):
        pass

    def findFile(self, fileID):
        pass

    def uploadFile(self, userpath):
        if(path.exists(userpath)):
        # check upload
            upload_successful = True
            if(upload_successful):
                return 0
            else:
                raise ValueError("Upload fail")
        else:
            raise ValueError("File does not exist")

    def login(self):
        pass

 
class File:
    def __init__(self, filename):
        self.fileID = 0 # will be assigned
        self.userID = 0;  # how to link userID here?
        self.name = filename
        self.fileformat = 'pdf'
        self.filepath = 'a/path'
        self.lastmodified = 'March-19-2023'

        # implicitly creating users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor
        global fileid 

        if fileid in fileid_list:
            fileid += 1
        if fileid < MAX_FILES:
            self.fileID = fileid
            # userid_list.append(userid)
            # To change the value of a global variable inside a function, refer to the variable by using the global keyword
            fileid += 1
            self.name = filename
            insert_data = [self.fileID, self.userID, self.filename, self.fileformat, self.filepath, self.lastmodified]

            fileid_list.append(fileid)
            
            try:
                news_cur.execute("INSERT INTO file VALUES (?, ?, ?, ?, ?, ?)", insert_data)
                news_con.commit()
            except news_con.Error:
                # Rolling back in case of error
                # print('user db insertion error')
                news_con.rollback()
                raise ValueError("file DB insertion error")
        else:
            raise ValueError("Maximum number of files, storage full")

        news_con.close()

    def getAccount(self):
        pass




def main():


    pass

    # User("Name1")
    # User("Name2")



if __name__ == "__main__":
    # logger.info('In uploader main') # check logger functionality
    main()
