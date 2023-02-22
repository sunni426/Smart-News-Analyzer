'''

test nlp analysis

'''
from uploader import File
import numpy as np
import tracemalloc
import cProfile, pstats
import logging
import logging.config

# fileID should be stored internally
class NLPFile(File):
    def __init__(self, name):
        self.fileID = 0 # will be assigned
        self.name = name
        self.syntax = [] # or some sort of struct? 
        self.semantics = []
        self.sentiment = []
        self.keywords = []

    def getTest(self, fileID):
        # parse uploaded file into text format (a string) of class NLPFile, with new field
        pass
    
    def analyzeSyntax(self):
        # these fields will be stored in the syntax member of NLPFile
        keywords_syntax = []
        names = []
        locations = []
        institutions = []
        address = []
        paragraph_count = 0
        word_count = 0
        line_count = 0

        # to put: parsing implementation
        # storing in syntax

        syntax_fail = True

        if(syntax_fail):
            raise ValueError("Syntax analysis failed")
        else:
            return 0;


    def analyzeSemantics(self):
        # these fields will be stored in the semantics member of NLPFile
        keywords_semantics = []
        summaries = []
        labels = []

        # to put: analysis implementation
        # storing in semantics

        semantics_fail = True

        if(semantics_fail):
            raise ValueError("Semantics analysis failed")
        else:
            return 0;


    def analyzeSentiment(self):
        # these fields will be stored in the sentiment member of NLPFile
        positives = []
        negatives = []
        neutrals = []

        # to put: analysis implementation
        # storing in sentiment

        sentiment_fail = True

        if(sentiment_fail):
            raise ValueError("Sentiment analysis failed")
        else:
            return 0;


def main():

    pass



if __name__ == "__main__":
    main()





'''

getText(fileID)
    Returns textID if successful: associated with the file but in the specific text format that this application supports for subsequent NLP analysis
analyzeSyntax(fileID)
Returns syntaxID if successful
    Stores info with fileID, accessible by syntaxID
analyzeSemantics(fileID)
Returns semanticsID if successful
    Stores info with fileID, accessible by semanticsID
analyzeSentiment(fileID)
    Returns sentimentID if successful
Stores info with fileID, accessible by sentimentID
    display(fileID, mode)
    mode: syntax, semantics, or sentiment


def getText(fileID):
    if PDF
    if image


# extract PDF XML format https://towardsdatascience.com/how-to-extract-data-from-pdf-forms-using-python-10b5e5f26f70 
import PyPDF2 as pypdf
def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value=haystack[key]
        except:
            continue
        if key==needle:
            return value
        if isinstance(value,dict):            
            x=findInDict(needle,value)            
            if x is not None:
                return x
pdfobject=open('CTRX_filled.pdf','rb')
pdf=pypdf.PdfFileReader(pdfobject)
xfa=findInDict('/XFA',pdf.resolvedObjects)
xml=xfa[7].getObject().getData()



# Extract Text from Image using Python - Tesseract is an open source OCR (optical character recognition)
    with Two Python libraries:
        pytesseract
        pillow
    https://pyshark.com/extract-text-from-image-using-python/ 


'''