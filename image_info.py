import cv2

image = cv2.imread("assets/sample_image.png")

image_shape = image.shape

width = image_shape[1]
height = image_shape[0]
channels = image_shape[2]

print("Width: ", width)
print("Height: ", height)
print("Channels: ", channels)
