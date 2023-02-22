from re import L
from uploader import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config


def test_file_exists():
    userpath = "hello!!!"
    with pytest.raises(ValueError, match="File does not exist"):
        uploadFile(userpath)
        
def test_login():
    username = "John"
    password = "Smith"
    with pytest.raises(ValueError, match="Password incorrect"):
        login(username, password)

# def test_upload():
#     userpath = "a_path"
#     with pytest.raises(ValueError, match="Upload fail") or pytest.raises(ValueError, match="File does not exist"):
#         uploadFile(userpath)
    # Q: if there are multiple check assertions (raise value errors) in one function, how to handle that as a unit test?