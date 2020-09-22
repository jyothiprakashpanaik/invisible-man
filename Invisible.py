# Import librarries 

import cv2
import numpy as np
import time 

# 0 represtent the in built web cam
cap = cv2.VideoCapture(0)
# time.sleep(5)

background = 0

# Captur the background
for i in range(10):
	
	ret,background = cap.read()
	# it will give the background color

while (cap.isOpened()):

	ret,img = cap.read()
	# it will give the current image

	if not ret:
		break 

	# hue Saturation Value
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	# Upper and Lower link (skin(red) color ranges from 0-30,150-180 in hsv)
	lower_red = np.array([0, 40, 40])
	upper_red = np.array([30, 255, 255])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)  # Seperating the clock part

	lower_red = np.array([150, 40, 40])
	upper_red = np.array([180, 255, 255])
	mask2 = cv2.inRange(hsv, lower_red, upper_red)  # Seperating the clock part
	mask1 = mask1 + mask2 # OR 1 or 0

	mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN, np.array((3,3)), iterations=2)
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8),iterations=1)

	mask2 = cv2.bitwise_not(mask1) # Every thing excet the cloak

	res1 = cv2.bitwise_and(background, background, mask=mask1)
	res2 = cv2.bitwise_and(img, img, mask=mask2)
	final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

	cv2.imshow('Harry Potter cloak',final_output )
	k = cv2.waitKey(10)

	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()






