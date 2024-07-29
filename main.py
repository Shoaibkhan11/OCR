import easyocr
import cv2
import os
import matplotlib.pyplot as plt


def ocr_predict(image_path):
    img=cv2.imread(image_path)
    reader=easyocr.Reader(['en'],gpu=False)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=reader.readtext(img)
    extractedText=' '.join([text for i,text,j in result])
    return extractedText


#extractedText=ocr_predict('text.jpg')
#print(extractedText)
#with open('text.txt','w') as f:
#    f.write(extractedText)
