from re import L
from nlp import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config
import sqlite3


def test_syntax():
    file1 = NLPFile("file1")
    with pytest.raises(ValueError, match="Syntax analysis failed"):
        file1.analyzeSyntax()
        
def test_semantics():
    file1 = NLPFile("file1")
    with pytest.raises(ValueError, match="Semantics analysis failed"):
        file1.analyzeSemantics()       

def test_sentiment():
    file1 = NLPFile("file1")
    with pytest.raises(ValueError, match="Sentiment analysis failed"):
        file1.analyzeSentiment()
        
