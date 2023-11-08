import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from cycler import cycler

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    background = photo[320:500, 450:560, 0:3].swapaxes(0, 1)
    
    cut = photo[320:500, 350:600, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()
    
    plt.imshow(background, origin='lower')
    
    
    plt.savefig(plotName)
    plt.show()

    return luma
 

readIntensity("yellow_tungsten.jpg", "Wwhite_processed.jpg", "Лампа дневного света", "белый лист")