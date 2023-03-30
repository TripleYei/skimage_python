import matplotlib.pyplot as plt
from skimage import io
import sys

argument = len(sys.argv)

imagen = sys.argv[1]


photo = io.imread(imagen)
plt.imshow(photo)
plt.show()




