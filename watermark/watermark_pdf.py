import PyPDF2

# Example of input: python watermark_pdf.py ../scripting/files/pdfs/ super.pdf wtr.pdf

import sys

path = sys.argv[1]
file_name = sys.argv[2]
watermark_file = sys.argv[3]

pdf = PyPDF2.PdfFileReader(open(path + file_name, 'rb'))
watermark = PyPDF2.PdfFileReader(open(path + watermark_file, 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf.getNumPages()):
  page = pdf.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open(path + 'watermarked_output.pdf', 'wb') as file:
    output.write(file)