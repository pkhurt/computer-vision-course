import cv2
import numpy as np
import argparse
from matplotlib import cm

## Global variables
n_markers = 10 # 0-9 markers available
current_marker = 1 # Color choice
marks_updated = False # Markers updated by watershed

def parse() -> str:
    parser = argparse.ArgumentParser(description="Pass your own picture to run the watershed custom seed algorithm on. \n " +
                                     "Once the pictures are shown, press a number (1-7) and click on the picture to segment an area with different colors.")
    parser.add_argument("--image", type=str, help="Path to the image")

    args = parser.parse_args()

    return args.image

def load_image(img_path: str):
    return cv2.imread(img_path)

def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

def create_list_of_colors(number_of_colors: int) -> list:
    colors = []
    for i in range(number_of_colors):
        colors.append(create_rgb(i))
    
    return colors

# Callback function
def mouse_callback(event, x, y, flags, images):
    global marks_updated

    marker_image, img_copy, colors = images # unpack the images & colors

    if event == cv2.EVENT_LBUTTONDOWN:
        # Markes passed to the watershed algo
        cv2.circle(marker_image, (x,y), 10, (current_marker), -1)

        # User sees on the image
        cv2.circle(img_copy, (x,y), 10, colors[current_marker], -1)

        marks_updated = True

def watershed_custom_seeds(img):
    global current_marker

    img_copy = np.copy(img)

    marker_image = np.zeros(img.shape[:2], dtype=np.int32)
    segments = np.zeros(img.shape, dtype=np.uint8)

    colors = create_list_of_colors(10)

    images_and_colors = (marker_image, img_copy, colors)

    # While image is open
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_callback, images_and_colors)

    while True:
        cv2.imshow("watershed segments", segments)
        cv2.imshow("image", img_copy)

        # Close all windows
        k = cv2.waitKey(1)
        if k == 27: # esc key pressed
            break

        # clearing all the colors press "c" key
        # resetting both images to the initial image
        elif k == ord("c"):
            img_copy = img.copy()
            marker_image = np.zeros(img.shape[:2], dtype=np.int32)
            segments = np.zeros(img.shape, dtype=np.uint8)

        # update color choice
        # get the keyboard press as character (like "2") and then get the integer
        # to be able to index colors[] list
        elif k > 0 and chr(k).isdigit():
            current_marker = int(chr(k))

        # update the markings
        if marks_updated:
            marker_image_copy = marker_image.copy()
            cv2.watershed(img, marker_image_copy)

            segments = np.zeros(img.shape, dtype=np.uint8)

            # coloring the index
            for color_index in range(n_markers):
                segments[marker_image_copy == (color_index)] = colors[color_index]

    cv2.destroyAllWindows()

if __name__ == "__main__":
    img_path = parse()
    img = load_image(img_path)
    watershed_custom_seeds(img)