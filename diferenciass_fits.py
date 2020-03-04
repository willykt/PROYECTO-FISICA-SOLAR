import sunpy
import numpy as np
import glob
from sunpy.map import Map
import matplotlib.pyplot as plt
from astropy.io import fits
import imageio



file_list = []
file_list.append(glob.glob('*.i*.fits'))
file_list=sorted(file_list)

files=Map(file_list)
#print(files)

ARRAY=[]
for i in range(10):
	ARRAY.append(files[i+1].data-files[i].data)

hdu = fits.PrimaryHDU(ARRAY)
hdulist = fits.HDUList([hdu])
hdulist.writeto('difference'+'.fits')
hdulist.close()





