from xmlrpc.server import DocXMLRPCRequestHandler
from docx2pdf import convert
from glob import glob

docxFile = glob("*.docx")
for i in docxFile:

    outputFile = f"{i[:-4]}.pdf"
    file = open(outputFile, "w")
    file.close()

    convert(i, outputFile)