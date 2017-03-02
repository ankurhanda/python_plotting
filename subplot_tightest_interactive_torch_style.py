import matplotlib.pyplot as plt
import numpy as np
import argparse
import read_sunrgbd_data


def tile_images(img, batch_size, rows, cols):
    batchImages = np.random.random((240*rows,320*cols,3))
    for i in range(rows):
        for j in range(cols):
            if i*cols+j < batch_size:
                batchImages[0+i*240:(i+1)*240,0+j*320:(j+1)*320,:] = img[i*cols+j]
            
    return batchImages
        


# Training settings
parser = argparse.ArgumentParser(description='plotting example')
parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                    help='input batch size for training (default: 64)')
                    
args = parser.parse_args()

rows = np.int(np.ceil(np.sqrt(args.batch_size)))
cols = np.int(np.ceil(args.batch_size / rows))

print('{0}, {1}'.format(rows,cols))

SUNRGBD_dataset = read_sunrgbd_data.dataset("SUNRGBD","/media/ankur/nnseg/sunrgbd_training.txt")
img, label = SUNRGBD_dataset.get_random_shuffle(args.batch_size)

batchImages = tile_images(img, args.batch_size, rows, cols)

#Random Image
someImage = np.random.random((240*np.int(rows),320*np.int(cols),3))

# Creare your figure and axes
fig,ax = plt.subplots(1)

# Set whitespace to 0
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

# Display the image
#ax.imshow(someImage[:,:,0],extent=(0,1,1,0))
ax.imshow(np.uint8(batchImages),extent=(0,1,1,0))

# Turn off axes and set axes limits
ax.axis('tight')
ax.axis('off')

plt.show()

