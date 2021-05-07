from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
from os.path import join
from os.path import exists

# Returns a list of the filepaths for the pdfs in path.
def getFiles(path):
    if not exists(path):
        raise FileNotFoundError
    
    path_list = [join(path, f) for f in listdir(path) if isPDF(f)]
    return path_list


def getFileNum(str, path):
    str = str.replace(path, '')
    return int(''.join([let for let in str if let in '0123456789']))

def sortFiles(path_list, path):
    filenumbers = {f : getFileNum(f, path) for f in path_list}
    filenumbers = sorted(filenumbers.items(), key=lambda x:x[1])
    return [i[0] for i in filenumbers]

    for k,v in filenumbers:
        print(f'{k}: {v}')



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










    

