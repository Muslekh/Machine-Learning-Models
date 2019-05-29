# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:23:13 2019

@author: user
"""

import PyPDF2 #importing library
f=open('pybook.pdf','rb')#reading a file
pdf_reader=PyPDF2.PdfFileReader(f)#fitting the read file to filereader
pdf_reader.numPages#getting the number of pages
page_one=pdf_reader.getPage(12) #will get the page 12
print(page_one.extractText()) #will print all the text in page 12
f.close() #will close the file

f=open('pybook.pdf','rb')#again we open thge file
pdf_reader=PyPDF2.PdfFileReader(f) #fitting the read file to filereader
first_page=pdf_reader.getPage(5)#getting page 5
pdf_writer=PyPDF2.PdfFileWriter()#importing writer to write
pdf_writer.addPage(first_page)#adding page number 5 to writer
pdf_output=open('testfile.pdf','wb')#creating a new pdf empty file
pdf_writer.write(pdf_output)#writing to output file
pdf_output.close() #close file
f.close() #close file



test=open('testfile.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(test)
pdf_reader.numPages()
f=open('pybook.pdf','rb')

#extracting all the text
pdf_text=[]
pdf_reader=PyPDF2.PdfFileReader(f)
for p in range(pdf_reader.numPages):
    page=pdf_reader.getPage(p)
    pdf_text.append(page.extractText())
f.close()
len(pdf_text)
