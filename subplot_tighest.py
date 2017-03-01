import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

def do_plot(ax):
    someImage = np.random.random((10,10,1))
    ax.imshow(someImage[:,:,0], interpolation='none')
    ax.set_axis_off()
    ax.autoscale_view('tight')

N = 11
cols = 4
rows = 4

gs = gridspec.GridSpec(rows, cols) 

fig = plt.figure()
plt.axis('off')
plt.subplot_tool()
plt.autoscale('tight')
for n in range(N):
    ax = fig.add_subplot(gs[n])
    do_plot(ax)
    plt.tight_layout()
    fig.show()
    plt.pause(0.00001);
    
plt.pause(1000)

