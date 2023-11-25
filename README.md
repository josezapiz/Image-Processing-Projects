# Image-Processing-Projects
&nbsp;&nbsp;&nbsp;&nbsp; University projects of the integrated master's Image Processing course

## Solirization exercise description
&nbsp;&nbsp;&nbsp;&nbsp; Using OpenCV, the function *solarize* is implemented for this exercise in order to be used for threshold values: 64, 128, 192 on an image that will first be converted to grayscale. 

&nbsp;&nbsp;&nbsp;&nbsp; Finally, the processed and unprocessed images will be stored in the folder.

| Cat Original | Gray | Solar64 | Solar128 | Solar192 |
| ------- | ------- | ------- | ------- | ------- |
| ![Image5](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/94c7986f-583a-4b77-b6df-5c30588e1d34) | ![Image 1](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/527c3447-33cc-47d6-8118-350d093c7c65) | ![Image 2](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/d3fe194a-b020-4c25-9373-45b9566f369a) | ![Image 3](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/8058eb85-efec-49d1-9236-bc1ea64417b0) | ![Image 4](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/12861be8-b0fe-4981-b6d6-13d48848a107) |


## Noise and filters description
&nbsp;&nbsp;&nbsp;&nbsp; The code implements the functions salt and pepper as well as poisson to add noise to an image that has been converted to grayscale. Afterwards, both different noise additions undergo the application of three different filters for noise removal: 
+ Median,
+ Gaussian Blur
+ Denoising (OpenCV fastNlMeansDenoising)

Subsequently, the filtered images are compared to the initial grayscale image using metrics for evaluation such as 
+ Structural Similarity Index (SSIM)
+ Mean Square Error (MSE)

| Original | Gray | Salt and Pepper | Poisson |
| ------- | ------- | ------- | ------- |
| ![horse](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/3c5c8e6d-4fe0-48fb-893e-99fe5d0be683) | ![Gray](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/07eef2b7-c854-4544-9c8d-b145024c31b9) | ![SaltPepper](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/ac2b833a-ccf0-4de4-99c1-c5f3b0bd57df) | ![Poisson](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/ff49c2c0-e0b7-4ee7-a41f-ebf59b0f1289) |

1) Filters on Salt and Pepper
    
| Median filter | Gaussian filter | fastNLDenoising |
| ------- | ------- | ------- |
| ![MedianSP](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/9d1122ba-a061-4e72-b2d2-d7ac0a478320) | ![Gauss Poisson](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/078f9029-8e01-49d1-be5a-dd58bb92e310) | ![fastNLSP](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/e25eb35d-e711-452a-ac91-7110073cff3a) |

2) Filters on Poisson

| Median filter | Gaussian filter | fastNLDenoising |
| ------- | ------- | ------- |
| ![Median Poisson](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/c4c18050-4422-45f1-9f30-0575b24f06af) | ![Gauss Poisson](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/52f98c21-b6fc-40a5-acdb-a5acee94fdb9) | ![fastNL Poisson](https://github.com/josezapiz/Image-Processing-Projects/assets/101471178/f914d808-9337-4972-8d05-5b5d27106589) |


| *SALT AND PEPPER* | SSIM | MSE |
| ------- | ------- | ------- |
| *Reference* | 1 | 1 |
| *Median filter* | 0.89 | 61.34 |
| *Gaussian filter* | 0.48 | 413.92 |
| *fastNLDenoising* | 0.028 | 401.35 |

| *POISSON* | SSIM | MSE |
| ------- | ------- | ------- |
| *Reference* | 1 | 1 |
| *Median filter* | 0.028 | 15681.49 |
| *Gaussian filter* | 0.907 | 5082.16 |
| *fastNLDenoising* | 0.097 | 4306.21 |


## Conclusion

&nbsp;&nbsp;&nbsp;&nbsp; After adding Salt and Pepper as well as Poisson noise to the images, it seems that Poisson noise is more intense. This was also evident when applying filters for noise removal. While in the case of Salt and Pepper noise, the median filter showed impressive noise reduction, there was no filter that effectively reduced the Poisson noise.

&nbsp;&nbsp;&nbsp;&nbsp; The Gaussian and fastNlDenoising filters significantly altered the images, causing them to become "blurry" to the extent that the content was almost indistinguishable in both Salt and Pepper and Poisson noise scenarios.








