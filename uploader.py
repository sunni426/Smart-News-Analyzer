'''

secure file uploader/ingester

'''

import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config
import os.path as path # https://docs.python.org/3/library/os.path.html
# import mysql.connector # need: pip install mysql-connector-python
import sqlite3

# implicitly creating users.db if not in cwd 
news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
news_cur = news_con.cursor() # to execute SQL statements, need DB cursor

# files_con = sqlite3.connect("files.db")
# files_cur = files_con.cursor() 

class File:
    def __init__(self, name):
        self.fileID = 0 # will be assigned
        self.name = name

    def getAccount(self):
        pass



# associated with user
class User:
    def __init__(self, userID, name):
        self.userID = userID;
        self.name = name;

    def setPassword(self):
        pass
    
    def viewFiles(self):
        pass

    def findFile(self, fileID):
        pass

    
# def login(username, password):
#     # stub
#     user_exists = True
#     password_incorrect = False
#     if(user_exists):
#         if(password_incorrect):
#             return 0
#         else:
#             raise ValueError("Password incorrect")
#     else:
#         raise ValueError("User does not exist")

def uploadFile(userpath):
    if(path.exists(userpath)):
        # check upload
        upload_successful = True
        if(upload_successful):
            return 0
        else:
            raise ValueError("Upload fail")
    else:
        raise ValueError("File does not exist")

# when you upload, have a uri: up to cloud. 




def main():

    pass



if __name__ == "__main__":
    main()

