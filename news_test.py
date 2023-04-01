from re import L
from news import *
from uploader import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3
import unittest


# to discuss: add a table to store this or not?

def test_getKeywords():
    file1 = NewsFile("file1")
    assert (getKeywords(file1) == [])

def test_searchGov():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Search Gov Fail"):
        searchGov(file1)

def test_searchWiki():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Search Wiki Fail"):
        searchWiki(file1)

def test_searchMedia():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Search Media Fail"):
        searchMedia(file1)

def test_findDefinitions():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Find Definitions Fail"):
        findDefinitions(file1)

def test_findContent():
    file2 = NewsFile("file2")
    with pytest.raises(ValueError, match="Find Content Fail"):
        findContent(file2)

def test_threading():
    file3 = NewsFile("file3")
    if __name__ == '__main__':
        unittest.main()