import numpy as np
import sys
import cv2
from pdf2image import convert_from_path
from PIL import Image

INPUT_PDF_PATH = None
OUTPUT_PDF_PATH = None

# Parameters changes based on document
Y_INDEX = 2080
Y_RANGE = 30
X_RANGE = 935
X_INDEX = 600

# Set it based on pixel value of watermark
THSD = 230

def no_watermark():

    # Converting PDF pages into images
    images = convert_from_path(INPUT_PDF_PATH)
    img0 = None
    res_images = []

    # img = np.array(images[6])
    # print(img.shape)
    # ----
    # _img = Image.fromarray(img)
    # _img.save("img.jpg")

    for i in range(len(images)):
        img = np.array(images[i])

        # If pixel values > threshold, set it to 255 [Removing Watermark]
        img[img > THSD] = 255

        # Whitening(255) a certain range in image (may vary from document to document)
        img[Y_INDEX:Y_INDEX+Y_RANGE, X_INDEX:X_INDEX+X_RANGE] = 255

        # Saving images
        _img = Image.fromarray(img)
        if i != 0:
            res_images.append(_img)
        else:
            img0 = _img

    # Merging images into PDF and saving as output
    img0.save(OUTPUT_PDF_PATH, save_all=True, append_images=res_images)  

# Driver
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERR, No input PDF Path!")
        exit(1)
    INPUT_PDF_PATH = sys.argv[1]
    OUTPUT_PDF_PATH = "No_Watermark_" + INPUT_PDF_PATH
    no_watermark()