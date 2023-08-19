import fitz
from PIL import Image

file_name = "my_file"
required_pages_sequence = "23 24 25 26 27 28"
required_pages = required_pages_sequence.split()
clean_pages = [int(p) for p in required_pages]
pdf_output_path = f"/home/X/Documents/{file_name}.pdf"
pdf_input_path = "/home/X/Documents/Docs.pdf"
doc = fitz.open(pdf_input_path)
img_list = []
for p in clean_pages:
    page = doc.load_page(p-1)
    pix = page.get_pixmap(dpi=150)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img_list.append(img)
if len(img_list) == 1:
    img_list[0].save(pdf_output_path)
else:
    img_list[0].save(pdf_output_path, save_all=True, append_images=img_list[1:])

