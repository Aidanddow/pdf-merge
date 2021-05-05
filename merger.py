from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
from os.path import join
from os.path import exists

# Returns a list of the filepaths for the pdfs in path.
def getFiles(path):
    if not exists(path):
        raise FileNotFoundError

    return [join(path, f) for f in listdir(path) if isPDF(f)]

# Adds each page in pdf to writer
def addPdf(fname, writer):
    pdf = PdfFileReader(fname,'rb')
    for n in range(pdf.getNumPages()):
        writer.addPage(pdf.getPage(n))

# Combines all of the pdfs in path_list
def mergeFiles(path_list):
    writer = PdfFileWriter()
    for f in path_list:
        addPdf(f,writer)
    return writer
    
# Returns a boolean denoting whether a file is a pdf
def isPDF(f):
    return f.endswith(".pdf")










    

