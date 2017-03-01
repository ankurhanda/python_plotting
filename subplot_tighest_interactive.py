import matplotlib.pyplot as plt
import numpy as np

#Random Image
someImage = np.random.random((10,10,1))

# Creare your figure and axes
fig,ax = plt.subplots(1)

# Set whitespace to 0
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

# Display the image
im1 = ax.imshow(someImage[:,:,0],extent=(0,1,1,0))

# Turn off axes and set axes limits
ax.axis('tight')
ax.axis('off')

fig.show();
for ii in range(1,30):
    someImage = np.random.random((10,10,1))
    im1.set_data(someImage[:,:,0]);
    im1.set_clim(vmin=someImage[:,:,0].min(), vmax=someImage[:,:,0].max())
    fig.show(); 
    plt.pause(1.00001);

#plt.show()

