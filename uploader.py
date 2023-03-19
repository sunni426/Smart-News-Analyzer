'''

secure file uploader/ingester

'''

import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config
import os.path as path # https://docs.python.org/3/library/os.path.html
import sqlite3

MAX_USERS = 1000 # max number users the system can support. can change values
userid = 1
# userid_list = []


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
    def __init__(self, name): # let userID be internal to this func and not as a param, 3/19
        # implicitly creating users.db if not in cwd 
        news_con = sqlite3.connect("news.db") # returns a Connection object, represents conntection to on-disk db
        news_cur = news_con.cursor() # to execute SQL statements, need DB cursor

        # if userid not in userid_list:
        global userid 
        if userid < MAX_USERS:
            self.userID = userid
            # userid_list.append(userid)
            # To change the value of a global variable inside a function, refer to the variable by using the global keyword
            userid += 1
            self.name = name
            insert_data = [self.userID, self.name]
            
            print(f'self.userID: {self.userID}, self.name: {self.name}')
            try:
                news_cur.execute("INSERT INTO user VALUES (?, ?)", insert_data)
                news_con.commit()
            except news_con.Error:
                # Rolling back in case of error
                print('user db insertion error')
                news_con.rollback()
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

# def uploadFile(userpath):
#     if(path.exists(userpath)):
#         # check upload
#         upload_successful = True
#         if(upload_successful):
#             return 0
#         else:
#             raise ValueError("Upload fail")
#     else:
#         raise ValueError("File does not exist")

# when you upload, have a uri: up to cloud. 




def main():

    # pass

    User("Name1")
    User("Name2")



if __name__ == "__main__":
    main()

