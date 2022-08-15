from pdf2image import convert_from_path

def convert_pdf(path):

    last_slash = path.rfind("\\")
    file_path = path[:last_slash+1]
    file_name = path[last_slash+1:]

    images = convert_from_path(r'{}.pdf'.format(path), 
    poppler_path=r'C:\poppler-0.68.0\bin')

    count = 1
    for im in images:
        im.save(r'{}\{}-{}.jpg'.format(file_path, file_name, count))
        count += 1
    print("converted")
path = input("Please write a file path: ")
convert_pdf(path)
