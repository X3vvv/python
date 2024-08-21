from PyPDF2 import PdfWriter, PdfReader

pwd = "password"
path = r"path\to\pdf"  # 这里填写目标 PDF 所在的路径

pdf_reader = PdfReader(path)
pdf_writer = PdfWriter()

for i in range(len(pdf_reader.pages)):
    # can further modify keeped pages
    pdf_writer.add_page(pdf_reader.pages[i])
pdf_writer.encrypt(pwd)  # 设置密码
with open(path, "wb") as out:
    pdf_writer.write(out)
