import PyPDF2

PDFfilename = "IPsec users_24Mar2020_24Mar2020.pdf" #filename of your PDF/directory where your PDF is stored

pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object

pg4 = pfr.getPage(1) #extract pg 127

writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
#add pages
writer.addPage(pg4)

NewPDFfilename = "allTables.txt" #filename of your PDF/directory where you want your new PDF to be
with open(NewPDFfilename, "wb") as outputStream:
    writer.write(outputStream) #write pages to new PDF