# Image-Compare-Tool

This tool compares images using Structural Similarity Index (SSIM) and Mean Squared Error (MSE) to give them similarity scores.

- A lower MSE score would denote a similar image with a score of 0 representing two images that are the same.
- An SSIM score ranges from 1 to -1, a score of 1 referring to identical images.
  By inputting a .csv file containing the file locations of your desired image pairs, the program will create an output.csv file (example below)
  containing the normalized SSIM score (1-SSIM), ranging from 0 to 2, and the elapsed time per image pair to run.

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

## References

1. https://www.geeksforgeeks.org/working-images-python/
2. https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
3. https://scikit-image.org/docs/dev/api/skimage.metrics.html#structural-similarity
4. https://pythonspot.com/files-spreadsheets-csv/
