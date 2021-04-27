# References:
# https://www.geeksforgeeks.org/working-images-python/
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
# https://scikit-image.org/docs/dev/api/skimage.metrics.html#structural-similarity
# https://pythonspot.com/files-spreadsheets-csv/

import cv2
from cv2 import cv2
import csv
import skimage 
from skimage.metrics import structural_similarity as ssim
import time
from time import process_time
import os.path
from os import path

images = []
inputpath = 'testing.csv'
if path.exists("imagesList.csv"):
	inputpath = 'imagesList.csv'

# read images from csv file and convert to grayscale
with open(inputpath, newline='') as csvfile:
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
		if image1.shape != image2.shape:
			if image1.size > image2.size:
				image1 = cv2.resize(image1, (image2.shape[1],image2.shape[0]))
			else:
				image2 = cv2.resize(image2, (image1.shape[1],image1.shape[0]))
		images.append((row[0],row[1],image1,image2))
		# print(', '.join(row))

# get mse and ssim with plot
with open('output.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',
						quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(["image1","image2","similar","elapsed"])
	for imagePair in images:
		# m,s = compare_images(imagePair[2], imagePair[3])
		t0= time.process_time()
		s = 1-ssim(imagePair[2], imagePair[3])
		filewriter.writerow([imagePair[0], imagePair[1],s,str(time.process_time() - t0)])



