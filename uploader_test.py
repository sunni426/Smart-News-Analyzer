from re import L
from uploader import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3

# import db_init

# def test_db_init():
#     db_init.main();

def test_login():
    pass

def test_user_db():
    filename = "logger.log"
    # file1 = NLPFile("file1_nlp")
    with pytest.raises(ValueError, match="File does not exist") or \
    pytest.raises(ValueError, match="user DB insertion error") or \
    pytest.raises(ValueError, match="Maximum number of users, storage full"):
        user1 = User("Name1")
        user1.uploadFile(filename)
        

def test_user_init():
    # with pytest.raises(ValueError, match="user DB insertion error"):
    user5 = User("Name5")
        

def test_upload():
    filename = "logger.log"
    user3 = User("Name3")
    with pytest.raises(ValueError, match="File does not exist") or \
    pytest.raises(ValueError, match="Upload fail"):
        user3.uploadFile(filename)