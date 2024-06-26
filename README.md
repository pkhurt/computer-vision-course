# computer-vision-course
# Sources & udemy course
<b>Udemy course:</b> https://www.udemy.com/share/10143y3@GmhgL2nFG3QDxH4DGeblXwsz6uiLPxBsfSLtQVXG8rsIo30x1YTrkmNiyJJGdCgVwA==/


## Environment setup
### Python Virtualenv 
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### Anaconda
#### Python Path
Add the conda to your python path:
```
export PATH="/home/peter/anaconda3/bin/:$PATH"
```

#### Open Anaconda terminal bash
```
source ~/anaconda3/bin/activate
```

#### Create the conda enviroment of the course
```
conda env create -f cvcourse_linux.yml
```

#### Activate and deactivate the created conda environment
```
# To activate this environment, use                                             
#     $ conda activate python-cvcourse                                          
# To deactivate an active environment, use                                                   
#     $ conda deactivate   
```
---
### Google Colab
Google colab already has the environment set up to all the needs of the udemy course.
Packages needed:
* matplotlib
* cv2
* Image
* numpy
#### Create a google colab file
Go to your google drive account and click on the three stripes on the top left. Then click "more". You should see now Google Colab as a creatable file.

This will create you a python notebook that is stored in your google drive. You can sync it also with your GitHub Account and give it access to your google drive data.

## Sections
### 1 - Numpy and image basics
This section covers all the numpy and image basics that you need to get started. 
#### Summary & Notebook
> **_NOTEBOOK:_** [section_1_numpy_and_image.ipynb](https://github.com/pkhurt/computer-vision-course/blob/main/section_1_numpy_and_image.ipynb)

```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from PIL import Image

plt.imhshow(image)  # Most used command to show images throughout the lectures
```
### 3 - Image Basics With OpenCV
This section covers opening and storing images, as well as drawing on images and mouse click events to draw on images.
#### Summary & Notebooks
> **_NOTEBOOK:_** [section_3_opening_files_with_openCv_script.py](https://github.com/pkhurt/computer-vision-course/blob/main/section_3_opening_files_with_openCv_script.py)
```python
import cv2

img = cv2.imread(DATA_DIR)
while True:
  cv2.imshow("image_name", img)
  cv2.waitKey(1) & 0xFF == 27:   # This stops the while loop when pressing the "esc" key
    break
cv2.destroyAllWindows()    #  This closes the window
```
> **_NOTEBOOK:_** [section_3_opening_files_with_openCv_script.py](https://github.com/pkhurt/computer-vision-course/blob/main/section_3_opening_files_with_openCv_script.py)
```python
# OpenCV and matplotlib have different order of the color channels
# matplotlib -> RGB: Red, Green, Blue
# OpenCV -> BGR: Blue, Green, Red
rgb_colored_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB) # conversion between color channels

# Read image in grayscale
img_grayscale = cv2.imread(DATA_DIR, cv2.IMREAD_GRAYSCALE)

# Resizing an image
resized_img = cv2.resize(rgb_colored_img, (1000, 400)) # fixed values
resized_img = cv2.resize(rgb_colored_img, (0,0),fix_img,width_ratio,height_ratio) # with a ratio

# flipping an image
cv2.flip(img, 0) # Around the x axis

```

### Object Tracking
#### Optical Flow
<!-- TODO: Describe shortly whats on: https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html -->
<!-- TODO: Describe shortly the things used in section_7_57_...ipynb and scripts/object_tracking_with_webcam -->