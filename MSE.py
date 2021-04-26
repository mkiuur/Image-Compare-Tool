# References:
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/

# using mse will require installing numpy, numpy is not a part of this packages requirements
# to run mse instead of ssim, numpy will need to be installed

import numpy as np

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err