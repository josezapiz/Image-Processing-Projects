import random
import os #for saving the pictures
import cv2 #'4.4.0'
import numpy as np

from skimage.metrics import structural_similarity as ssim


def sp_noise(image,prob):
    #add salt and pepper
    output = np.zeros(image.shape, np.uint8) #canvas
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])	
	# the lower the error, the more "similar"
    return err


#read image
original = cv2.imread('horse.png')
gray_image = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# show the original
cv2.imshow('Original image',original)
cv2.imshow('Gray image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#+++++++++++++++ MARINATING +++++++++++++++++++++

#marinating with 10% of salt and pepper 
noisyImage = sp_noise(gray_image, 0.1)
cv2.imshow("Salt and Pepper Image", noisyImage)

#marinating with Poisson's recipe
poissonNoise = np.random.poisson(gray_image / 255.0 * 1) /1 * 255
cv2.imshow("Poisson Image", poissonNoise)

#+++++++++++++++++++++++++++++++++++++++++++++++++++

cv2.waitKey(0)
cv2.destroyWindow('Poisson Image')


#++++++++++++++ APPLYING FILTERS ++++++++++++++++++++++++++++

#median filter for Salt and Pepper
median = cv2.medianBlur(noisyImage,5)
cv2.imshow("Median on SP", median)

#GaussianBlur for Salt and Pepper
blur = cv2.GaussianBlur(noisyImage,(7,7),0)
cv2.imshow("Gaussian on SP", blur)

#Denoising for Salt and Pepper
nl = cv2.fastNlMeansDenoising(noisyImage,None, 50.0)
cv2.imshow("fastNL on SP",nl)
cv2.waitKey(0)
cv2.destroyAllWindows()

#median filter for Poisson
cv2.imshow("Poisson Image", poissonNoise)
poissonNoise = np.floor(np.abs(poissonNoise)).astype('uint8')
medianP = cv2.medianBlur(poissonNoise,3)
cv2.imshow("Median on Poisson", medianP)

#GaussianBlur for Poisson
blurP = cv2.GaussianBlur(poissonNoise,(3,3),0)
cv2.imshow("Gaussian on Poisson", blurP)

#Denoising for Poisson
nlP = cv2.fastNlMeansDenoising(poissonNoise,None, 80.0)
cv2.imshow("fastNL on Poisson",nlP)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

cv2.waitKey(0)
cv2.destroyAllWindows()



compare_none = ssim(gray_image,gray_image)
print("Reference" , compare_none )

#++++++++++++ SSIM FOR SALT AND PEPPER WITH GRAY_IMAGE ++++++++++++

compare_median = ssim(gray_image, median)
print("SSIM Median:" , compare_median )
compare_gauss = ssim(gray_image, blur)
print("SSIM Gauss:" , compare_gauss)
compare_NL = ssim(gray_image, nl)
print("SSIM NL:" , compare_NL)

#++++++++++++ SSIM FOR POISSON WITH GRAY_IMAGE ++++++++++++

Pcompare_median = ssim(gray_image, medianP)
print("SSIM Poisson Median:" , Pcompare_median )
Pcompare_gauss = ssim(gray_image, blurP)
print("SSIM Poisson Gauss:" , Pcompare_gauss)
Pcompare_NL = ssim(gray_image, nlP)
print("SSIM Poisson NL:" , Pcompare_NL)


#++++++++++++ MSE FOR SALT AND PEPPER ++++++++++

mse_median = mse(gray_image,median)
print("MSE MEDIAN:", mse_median)
mse_gauss = mse(gray_image,blur)
print("MSE GAUSS:", mse_gauss)
mse_NL = mse(gray_image, nl)
print("MSE NL:", mse_NL)

#++++++++++++ MSE FOR POISSON ++++++++++

Pmse_median = mse(gray_image,medianP)
print("MSE POISSON MEDIAN:", Pmse_median)
Pmse_gauss = mse(gray_image,blurP)
print("MSE POISSON GAUSS:", Pmse_gauss)
Pmse_NL = mse(gray_image, nlP)
print("MSE POISSON NL:", Pmse_NL)


#++++++++++++++++++++++ Saving Images ++++++++++++++++++++++++++++++
directory = r'<path>'
filename1 = "Gray.jpg"
filename2 = "SaltPepper.jpg"
filename3 = "Poisson.jpg"
filename4 = "MedianSP.jpg"
filename5 = "GaussSP.jpg"
filename6 = "fastNLSP.jpg"
filename7 = "Median Poisson.jpg"
filename8 = "Gauss Poisson.jpg"
filename9 = "fastNL Poisson.jpg"

os.chdir(directory)

cv2.imwrite(filename1, gray_image)
cv2.imwrite(filename2, noisyImage)
cv2.imwrite(filename3, poissonNoise)
cv2.imwrite(filename4, median)
cv2.imwrite(filename5, blur)
cv2.imwrite(filename6, nl)
cv2.imwrite(filename7, medianP)
cv2.imwrite(filename8, blurP)
cv2.imwrite(filename9, nlP)
