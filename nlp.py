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