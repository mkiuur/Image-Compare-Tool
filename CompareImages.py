# References:
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/

import skimage
# from skimage import measure as mm
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import MSE
from MSE import mse
import time

def compare_images_plot(imageA, imageB, title):

	t0= time.process_time()

	# compute the mean squared error and structural similarity
	m,s = compare_images(imageA, imageB)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# compute elapsed time
	elapsed = time.process_time() - t0

	# show the images
	plt.show()

	# return mse, ssim, elapsed time
	return m, s, elapsed

def compare_images(imageA,imageB):
	return mse(imageA, imageB),ssim(imageA, imageB)
	