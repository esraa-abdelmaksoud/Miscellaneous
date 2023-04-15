import cv2
import os
import fitz

pdf_path = '/mnt/D/текст_отчета_14-7.pdf'
rect_dir = '/mnt/D/rect_images/'
image_path = '/mnt/D/текст_отчета_14-7.png'

def extract_data(pdf_path: str):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    text_list = page.get_text("blocks")
    doc.close()
    return text_list

def draw_rects(image_path: str, rect_dir: str, text_list: list):
    print('img path', image_path)
    img = cv2.imread(image_path)
    print(text_list)
    # -1 to skip page image
    for i in range(len(text_list)-1):
        p0,p1 = (int(text_list[i][0]), int(text_list[i][1])), (int(text_list[i][2]), int(text_list[i][3]))
        text = text_list[i][4]
        print(p0,p1)
        # print(text)
        cv2.rectangle(img, p0, p1, (0, 255, 0), thickness=3)
    _, tail = os.path.split(image_path)
    output_path = os.path.join(rect_dir,tail)
    print(output_path)
    cv2.imwrite(output_path, img)

text_list = extract_data(pdf_path)
print(text_list)
draw_rects(image_path, rect_dir, text_list)
