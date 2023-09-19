import re
from pdf2image import convert_from_path
import pytesseract
from pytesseract import Output

def pdf_image():
    pages=convert_from_path("Vishali Nagalingam.pdf",poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    for indx,img in enumerate(pages):
        img.save(f"demo-{indx}.jpg")
#pdf_image()


def ocr_process(image):
    try:
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        #data = pytesseract.pytesseract.image_to_string(image)
        data = pytesseract.pytesseract.image_to_data(image, output_type=Output.DICT)
        #for text in data.split(' '):
             #print(text)
        # ' '.join(data['text'])
        for txt in data['text']:
            data = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", txt)
            if data:
                print(data)
            #print(txt)
        # print(data)

    except Exception as e:
        print(e)

img_path = r'C:\Users\user\Documents\new_update\demo-0.jpg'
ocr_process(img_path)