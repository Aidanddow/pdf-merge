from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
from os.path import join
from os.path import exists

# Recieve file path
# Look for pdfs
# read pdfs
# add to common pdf

def getFiles(path):
    if not exists(path):
        raise FileNotFoundError

    return [join(path, f) for f in listdir(path) if isPDF(f)]


def addPdf(fname, writer):
    pdf = PdfFileReader(fname,'rb')
    for n in range(pdf.getNumPages()):
        writer.addPage(pdf.getPage(n))


def mergeFiles(path_list):
    writer = PdfFileWriter()
    for f in path_list:
        addPdf(f,writer)
    return writer
    

def isPDF(f):
    return f.endswith(".pdf")










    

