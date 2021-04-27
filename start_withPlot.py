# References:
# https://www.geeksforgeeks.org/working-images-python/
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
# https://scikit-image.org/docs/dev/api/skimage.metrics.html#structural-similarity
# https://pythonspot.com/files-spreadsheets-csv/


import CompareImages
from CompareImages import compare_images_plot
import matplotlib.pyplot as plt
# import PIL
# from PIL import Image
import cv2
from cv2 import cv2
import csv
import numpy as np
import time
import os.path
from os import path


images = []

# set default input path to testing.csv file
inputpath = 'testing.csv'

# change input path to images list if .csv file exists in project directory
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
		
		# get image names from absolute paths for plots
		image1Name = row[0].split("/")[-1]
		image2Name = row[1].split("/")[-1]

		# add image pairs and names to data structure 'images'
		images.append((image1Name,image2Name,image1,image2))
		# print(', '.join(row))

# open or create output.csv file
with open('output.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',
						quotechar='|', quoting=csv.QUOTE_MINIMAL)
	
	# create table headers
	filewriter.writerow(["image1","image2","similar","elapsed"])
	
	# for each image pair, get mse, ssim, and show plots
	for imagePair in images:
		title = imagePair[0] + " vs. " + imagePair[1]
		m,s,elapsed = compare_images_plot(imagePair[2], imagePair[3], title)

		# add image names, ssim, elapsed time to csv file 
		filewriter.writerow([imagePair[0], imagePair[1],s,str(elapsed)])
