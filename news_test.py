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

def test_ingest_feed():

    url = 'https://rss.art19.com/apology-line'
    user5 = User("Name5")

    try:
        title = "The Apology Line"
        ingest_title, summary, link_type = user6.uploadFile(filename)
        self.assertEqual(title, ingest_title)
    except:
        pytest.raises(ValueError, match="Error storing feed ingester contents")