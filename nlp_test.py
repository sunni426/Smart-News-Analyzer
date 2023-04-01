from re import L
from nlp import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3
import unittest
import functions


def test_syntax():
    file1 = NLPFile("file1_nlp")
    with pytest.raises(ValueError, match="Syntax analysis failed"):
        file1.analyzeSyntax()
        
def test_semantics():
    file2 = NLPFile("file2_nlp")
    with pytest.raises(ValueError, match="Semantics analysis failed"):
        file2.analyzeSemantics(0)       

def test_sentiment():
    file3 = NLPFile("file3_nlp")
    with pytest.raises(ValueError, match="Sentiment analysis failed"):
        file3.analyzeSentiment(0)
        
def test_threading():
    file4 = NLPFile("file4_nlp")
    if __name__ == '__main__':
        unittest.main()
