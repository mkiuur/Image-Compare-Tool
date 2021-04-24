# References:
# https://www.geeksforgeeks.org/working-images-python/
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
# https://scikit-image.org/docs/dev/api/skimage.metrics.html#structural-similarity

import CompareImages
from CompareImages import compare_images
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import cv2
from cv2 import cv2


# load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("images/rgb.png")
desaturated = cv2.imread("images/desaturated.png")
shopped = cv2.imread("images/composite.png")
# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
desaturated = cv2.cvtColor(desaturated, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("Desaturated", desaturated), ("Photoshopped", shopped)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images
compare_images(original, original, "Original vs. Original")
compare_images(original, desaturated, "Original vs. Contrast")
compare_images(original, shopped, "Original vs. Photoshopped")