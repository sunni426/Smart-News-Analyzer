from uploader import *
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config


def test_file_exists():
    userpath = "hello!!!"
    with pytest.raises(ValueError, match="File does not exist"):
        uploadFile(userpath);
        
