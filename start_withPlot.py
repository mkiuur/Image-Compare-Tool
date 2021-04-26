# References:
# https://www.geeksforgeeks.org/working-images-python/
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
# https://scikit-image.org/docs/dev/api/skimage.metrics.html#structural-similarity

import CompareImages
from CompareImages import compare_images_plot
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import cv2
from cv2 import cv2
import csv
import numpy as np

images = []

# read images from csv file
with open('ImagesList.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		try:
			image1 = cv2.imread(row[0])
			image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
		except:
			print("could not load image: " + str(row[0]))
			continue
		try:
			image2 = cv2.imread(row[1])
			image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
		except:
			print("could not load image: " + str(row[1]))
			continue

		# make sure images are the same size and if not, resize
		# make sure images are the same size and if not, resize
		if image1.size != image2.size:
			if image1.size > image2.size:
				image1 = cv2.resize(image1, (image2.shape[1],image2.shape[0]))
			else:
				image2 = cv2.resize(image2, (image1.shape[1],image1.shape[0]))
		image1Name = row[0].split("/")[-1]
		image2Name = row[1].split("/")[-1]
		images.append((image1Name,image2Name,image1,image2))
		print(', '.join(row))

# get mse and ssim with plot
for imagePair in images:
	title = imagePair[0] + " vs. " + imagePair[1]
	compare_images_plot(imagePair[2], imagePair[3], title)