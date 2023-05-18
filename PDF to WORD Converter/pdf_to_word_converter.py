from pdf2docx import Converter

old_pdf = "Enter the file name you want to convert"
new_docx = "new.docx"

obj = Converter(old_pdf)
obj.convert(new_docx)
obj.close()