import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

dir1 = '/Volumes/TIM/Lab2/Oct3/'
dir2 = '/Volumes/TIM/Lab2/Oct7/'
dir3 = '/Volumes/TIM/Lab2/CCD/'

### Section 1.2

bias1 = fits.open(dir1+'oct3-001b.fits')
 
print bias1.info ()

print (type(bias1))

image1= bias1[0].data
print (type(image1))
print image1.shape

bins = np.arange(1150,1250)
plt.imshow(image1, interpolation = 'None')
plt.hist(image1)
plt.hist(image1.reshape(1024*1024), bins)
plt.xlim(1150,1250)

nfiles_b = 11
nfiles_v = 11
nfiles_r = 11
nfiles_nf=49

npixelsx= 1024
npixelsy = 1024

bias_image_b = np.zeros((npixelsx,npixelsy, nfiles_b))
bias_image_v = np.zeros((npixelsx,npixelsy, nfiles_v))
bias_image_r = np.zeros((npixelsx,npixelsy, nfiles_r))
bias_image_nf = np.zeros((npixelsx,npixelsy, nfiles_nf))
# get data for blue filter from october 3rd
for i in range (1,10):
    bias_image_b[:,:,i-1] = fits.getdata(dir1+'oct3-00'+str(i) +'b.fits')  
for i in range (10,12):
    bias_image_b[:,:,i-1] = fits.getdata(dir1+'oct3-0'+str(i) +'b.fits')

# get data for visible filter from october 3rd
for i in range (1,10):
    bias_image_v[:,:,i-1] = fits.getdata(dir1+'oct3-00'+str(i) +'v.fits')  
for i in range (10,12):
    bias_image_v[:,:,i-1] = fits.getdata(dir1+'oct3-0'+str(i) +'v.fits')

# get data for red filter from october 3rd
for i in range (1,10):
    bias_image_r[:,:,i-1] = fits.getdata(dir1+'oct3-00'+str(i) +'r.fits')  
for i in range (10,12):
    bias_image_r[:,:,i-1] = fits.getdata(dir1+'oct3-0'+str(i) +'r.fits')

# get data for no filter from october 3rd
for i in range (1,10):
    bias_image_nf[:,:,i-1] = fits.getdata(dir1+'oct3-00'+str(i) +'nf.fits')  
for i in range (10,50):
    bias_image_nf[:,:,i-1] = fits.getdata(dir1+'oct3-0'+str(i) +'nf.fits')




### Section 2.1 (Bias)
bias = np.zersos(1024,1024,10)

for i in range (1,11):
    bias[:,:i-1] = fits.getdata(dir3+'sec2_1-00'+str(i)+'bias.fits')
bias_mean = np.mean(bias)
print bias_mean
### Section 2.2


### Section 2.3


### Section 2.4


### Section 2.5


### Section 2.6