import cv2 #'4.4.0'
import numpy as np
import os #for saving the pictures


#solarize function
def solarize(image,thresValue):
    output = np.zeros(image.shape,np.uint8) #creating canvas 
    for i in range(image.shape[0]): #scanning the image and comparing with thres
        for j in range(image.shape[1]):
            if image[i][j] < thresValue: 
                output[i][j] = 255 - image[i][j] 
            else:
                output[i][j] = image[i][j]
    return output


#read image
original = cv2.imread('cat.jpg')
gray_image = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# show the original
cv2.imshow('Original image',original)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Solarization by required threshold (calling the function)
solar64 = solarize(gray_image,64)
solar128 = solarize(gray_image,128)
solar192 = solarize(gray_image,192)

#printing
cv2.imshow('Gray image', gray_image)
cv2.imshow('Solarization by 64', solar64)
cv2.imshow('Solarization by 128', solar128)
cv2.imshow('Solarization by 192', solar192)

cv2.waitKey(0)
cv2.destroyAllWindows()

#saving images
directory = r'<path>'
filename1 = "Gray.jpg"
filename2 = "Solar64.jpg"
filename3 = "Solar128.jpg"
filename4 = "Solar192.jpg"
os.chdir(directory)
cv2.imwrite(filename1, gray_image)
cv2.imwrite(filename2, solar64)
cv2.imwrite(filename3, solar128)
cv2.imwrite(filename4, solar192)


