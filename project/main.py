import pytesseract as pyt
import cv2

img=cv2.imread("text_img.png")

pyt.pytesseract.tesseract_cmd=r"C:\Users\Shruti\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

text=pyt.image_to_string(img)

print(text)

