from pdf2image import convert_from_path
pages = convert_from_path('pdftest.pdf', 500)

pictures = 0
for page in pages:
    pictures = pictures + 1
    page.save (str(pictures) + '.jpg','JPEG')
    
