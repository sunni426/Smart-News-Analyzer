from re import L
from uploader import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3


def test_file_exists():
    userpath = "hello!!!"
    with pytest.raises(ValueError, match="File does not exist"):
        user1 = User("Name1")
        user1.uploadFile(userpath)
        

def test_user_init():
    with pytest.raises(ValueError, match="Maximum number of users, storage full"):
        user2 = User("Name2")

# def test_login():
#     username = "John"
#     password = "Smith"
#     with pytest.raises(ValueError, match="Password incorrect"):
#         login(username, password)

def test_upload():
    userpath = "news-analyzer-sunni426"
    # with pytest.raises(ValueError, match="Upload fail"):
    #     uploadFile(userpath)
    # with pytest.raises(ValueError, match="File does not exist"):
    #     uploadFile(userpath)
    # with pytest.raises(ValueError, match="Upload fail") or pytest.raises(ValueError, match="File does not exist"):
    #     uploadFile(userpath)
    # # Q: if there are multiple check assertions (raise value errors) in one function, how to handle that as a unit test?