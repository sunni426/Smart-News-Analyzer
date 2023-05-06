from re import L
from uploader import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3
import os
import os.path as path
import time
import login
from datetime import date
import json

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
        file, contents = user1.uploadFile(filename)
        

def test_user_init():
    # with pytest.raises(ValueError, match="user DB insertion error"):
    user5 = User("Name5")
        

def test_upload_fail():
    filename = "loggerrrrrr.log"
    user3 = User("Name3")
    with pytest.raises(ValueError, match="File does not exist") or \
    pytest.raises(ValueError, match="Upload fail"):
        contents = user3.uploadFile(filename)


def test_upload_sunny():
    filename = "logger.log"
    user6 = User("Name6")

    with open(filename, "w") as file:
        file.write("test")

    try:
        with open(filename, "r") as file:
            file, contents = user6.uploadFile(filename)
            self.assertEqual(contents, "test")
    except FileNotFoundError:
        pytest.raises(ValueError, match="File does not exist")
    except:
        pytest.raises(ValueError, match="Upload fail")

    # cleanup
    os.remove(filename)
