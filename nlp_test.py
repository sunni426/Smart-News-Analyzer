from re import L
from nlp import *
from uploader import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3
import unittest


# format = "%(asctime)s: %(message)s"
# logging.basicConfig(format=format, level=logging.INFO, filename='logger.txt',
#     filemode='w', datefmt="%H:%M:%S")


# def test_syntax():
#     file1 = NLPFile("file1_nlp")
#     with pytest.raises(ValueError, match="Syntax analysis failed"):
#         file1.analyzeSyntax()
        
def test_semantics():
    file2 = NLPFile("file2_nlp")
    with pytest.raises(ValueError, match="Semantics analysis failed"):
        analyzeSemantics(file2, 0)       

def test_sentiment():
    file3 = NLPFile("file3_nlp")
    with pytest.raises(ValueError, match="Sentiment analysis failed"):
        analyzeSentiment(file3,0)
        
def test_threading():
    file4 = NLPFile("file4_nlp")
    # logger.debug('This is a debug message in test_threading')
    if __name__ == '__main__':
        unittest.main()
