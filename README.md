# Image-Compare-Tool

This tool compares images using Structural Similarity Index (SSIM) and Mean Squared Error (MSE) to give them similarity scores.

- A lower MSE score would denote a similar image with a score of 0 representing two images that are the same.
- An SSIM score ranges from 1 to -1, a score of 1 referring to identical images.
  By inputting a .csv file containing the file locations of your desired image pairs, the program will create an output.csv file (example below) containing the normalized SSIM score (1-SSIM), ranging from 0 to 2, and the elapsed time per image pair to run.

Example output.csv file:
| image1 | image2 | similar | elapsed |
| ------ | ------ | ------- | ------- |
| aa.png | ba.png | 0 | 0.006 |
| ab.png | bb.png | 0.23 | 0.843 |
| ac.png | bc.png | 0 | 1.43 |
| ad.png | bd.png | 1 | 2.32 |

## Installation

1. Clone the repository
2. Install the project's dependencies by running `pip install -r requirements.txt`

## Usage

1. Add input 'imagesList.csv' file to project directory containing image pair absolute paths
2. Run `python3 ./start.py` to start the program, or `python3 ./start_withPlot.py` to run the program and view the images pairs, MSE, and SSIM.
3. Once the program has finished, retrieve 'output.csv' file from project directory

## Testing

Test images have been included in the subfolder /images and a 'testing.csv' file has been included. This will be the default
input file if no 'imagesList.csv' is included in the project directory.
![plotExample](/images/plotExample.png)

## Design Process

- Began development on MAC in VSCode. Chose to use python because of it's large amount of existing automation libraries
- Searched for existing python libraries relevant to image comparison, found Structural Similarity Index (SSIM) and Mean Squared Error (MSE) tutorials (2).
- Implemented both according to tutorial but decided to use SSIM for output results because structural similarity seems more accurate.
- Tested SSIM and MSE with grayscale test images including a comparison of the same image, desaturated version of the same image, a version of the image with photoshopped elements added on top, and a resizing of the same image.
- Implemented reading absolute and relative file locations from a .csv file into the existing code.
- Separated out the example code from the tutorial into a start function that would just provide the output .csv file and a version that would show the images being compared side by side, as well as both their MSE and SSIM scores, as seen in the tutorial. This reduces elapsed time per image to just how long it takes to run the SSIM.
- Put the opening of images from a .csv file into a try-except so that broken image paths would not crash the program.
- Added a few lines to find out if images were the same dimensions, and if not, to resize the larger image because MSE and SSIM only work on images of the same dimensions. This would be relevant in the case where identical images were being compared but were different sizes. Reducing the size of the larger image maintains more information than enlarging the smaller image.
- Implemented creating an output.csv file containing the absolute paths of the images the program was able to open, the SSIM scores for the image pairs, and the elapsed time for calculating the SSIM.
- Made the .csv file used for testing the default input file in case a custome input file has not been added to the project directory by a user.
- Added more comments and cleaned up the structure of the code for ease in maintenance and functionality additions.
- Explored wrapping the project with Docker to ease installation but would have required mounting the container directory on a local directory, decided against it due to time constraints.
- Tested installation and run on PC which failed. Debugged and deleted unused library 'Pillow' to solve the problem. Program now installs and runs successfully on MAC and PC but did require some debugging.
- Cleaned up README.md

## References

1. https://www.geeksforgeeks.org/working-images-python/
2. https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
3. https://scikit-image.org/docs/dev/api/skimage.metrics.html#structural-similarity
4. https://pythonspot.com/files-spreadsheets-csv/
