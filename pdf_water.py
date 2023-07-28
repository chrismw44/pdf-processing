import PyPDF2
import sys

water_input = sys.argv[1]
file_input = sys.argv[2]

wtr_file = PyPDF2.PdfReader(water_input)
watermark = wtr_file.pages[0]

input_file = PyPDF2.PdfReader(file_input)

writer = PyPDF2.PdfWriter()

for i in range(len(input_file.pages)):
    content_page = input_file.pages[i]
    content_page.merge_page(watermark)
    writer.add_page(content_page)

with open('watermarked.pdf', 'wb') as new_file:
    writer.write(new_file)
