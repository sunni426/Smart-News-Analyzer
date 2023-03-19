from re import L
from news import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3


def test_getKeywords():
    file1 = NewsFile("file1")
    assert (file1.getKeywords() == [])

def test_searchGov():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Search Gov Fail"):
        file1.searchGov()

def test_searchWiki():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Search Wiki Fail"):
        file1.searchWiki()

def test_searchMedia():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Search Media Fail"):
        file1.searchMedia()

def test_findDefinitions():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Find Definitions Fail"):
        file1.findDefinitions()

def test_findContent():
    file1 = NewsFile("file1")
    with pytest.raises(ValueError, match="Find Content Fail"):
        file1.findContent()