from pdf2image import convert_from_path

def convert_multi_pdf(file_name,pages):

    for page in range(pages):

        images = convert_from_path(r'D:\Lab images\{}.pdf'.format(file_name), 
        poppler_path=r'C:\poppler-0.68.0\bin')

        for i, im in enumerate(images):
            im.save(r'D:\Lab images\{}-{}.jpg'.format(file_name,i))

def convert_pdf (file_name):

    images = convert_from_path(r'D:\Lab images\{}.pdf'.format(file_name), 
    poppler_path=r'C:\poppler-0.68.0\bin')

    for im in images:
        im.save(r'D:\Lab images\{}.jpg'.format(file_name))

