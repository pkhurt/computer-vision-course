import cv2

img = cv2.imread("/home/peter/workspace/computer-vision-course/Computer-Vision-with-Python/DATA/00-puppy.jpg")

print(type(img))

while True:
    cv2.imshow("Puppy", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()