'''

secure file uploader/ingester

'''

import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config
import os.path as path # https://docs.python.org/3/library/os.path.html




class File:
    def __init__(self, fileID, name):
        self.fileID = fileID
        self.name = name

    def getAccount(self):
        pass

    # def 


# associated with user
class User:
    def __init__(self, accountID, name):
        self.accountID = accountID;
        self.name = name;

    def setPassword(self):
        pass
    
    def viewFiles(self):
        pass

    def findFile(self, fileID):
        pass

    

def uploadFile(userpath):
    if(path.exists(userpath)):
        return 0
    else:
        raise ValueError("File does not exist")

# def main():

#     # uploadFile("hello")
#     pass



# if __name__ == "__main__":
#     main()
