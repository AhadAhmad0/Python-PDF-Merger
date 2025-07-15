from PyPDF2 import PdfMerger

pdfs = ["Jf.pdf" , "Jf2.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()