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


data_images=[]
for i in range(3):
    data_images.append(np.abs(files[i+1].data-files[i].data))
    											


index = 0

def toggle_images(event):
    global index

    index += 1

    if index < len(data_images):
        plt.imshow(data_images[index])
        plt.colorbar()
	
        plt.draw()
    else:        
        plt.close()

#----------------------------------


plt.imshow(data_images[index],origin='bottom',animated=True)
plt.colorbar()
plt.title(files[i].date.value)
plt.connect('key_press_event', toggle_images)
#plt.savefig('files[i].date.value.pdf',dpi=300)
plt.show()


