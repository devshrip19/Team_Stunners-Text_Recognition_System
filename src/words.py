import argparse
import os
import cv2
import editdistance
import numpy as np
from PIL import Image
from DataLoaderIAM import DataLoaderIAM, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
from path import Path
import glob
# import pytesseract as pt
# pt.pytesseract.tesseract_cmd = r'C:\Users\ABHISHEK MOHARIR\AppData\Local\Tesseract.exe'


import cv2
import numpy as np

img = cv2.imread('/Users/alone_walker/Desktop/htr/SimpleHTR/my0.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((4,4), np.uint8)
imgMorph = cv2.erode(thresh1, kernel, iterations = 1)

contours, hierarchy = cv2.findContours(imgMorph,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

i=1
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)

    if w>10 and w<100 and h>10 and h<100:
        #save individual images
        cv2.imwrite("/Users/alone_walker/Desktop/htr/SimpleHTR/words/my{}.png".format((i)),thresh1[y:y+h,x:x+w])
        i=i+1
cv2.destroyAllWindows()
cv2.imshow('BindingBox',imgMorph)
cv2.waitKey(0)
cv2.destroyAllWindows()