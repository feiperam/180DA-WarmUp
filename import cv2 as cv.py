'''
1. Choose something that is relatively monochromatic with a color fairly different from
your background surroundings (a water bottle, a piece of clothing). Try to create
a video stream where you track this object with a bounding box surrounding it by
thresholding HSV or RGB values. Is HSV or RGB typically better? How large is the
threshold range that you need to track the object?

From this one lab demonstration I would say HSV is typically better, especially considering its robustness when dealing with external lighting changes.

2. Now change the lighting condition (turn on or off the lights or turn on your phone
flashlight on the object). Is there a major difference in the tracking ability of your
object?

yES when using my camera flash on my phone the video tracking was more accurate in isolating the desired colors within the boiundary box.

3. Now navigate to a Color Picker on your phone (Zoom into the color zone so that it
covers a good portion of your phone screen). Since you can pick your color with the
website, see if that is the color (with a small range) that you can pick up with your
camera. Does changing your phone brightness help or hurt with how your code is able
to track the color?

Increasing my phone brightness helps significantly with how my code is able to ttrack the target color.

4. Create a new piece of code that can determine the “dominant” color in a designated
(central) rectangle in your video feed (Use K-Means, see a tutorial to find an image's
dominant colors). Use your non-phone object and change the brightness of its sur-
roundings. Note the change of the color. Do the same with your phone. Is one or the
other more robust to brightness?

It seems that the phone screen is more robust to the change in lighting conditions.

'''
import cv2 as cv
import numpy as np
from PIL import Image
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,105,105])
    upper_blue = np.array([130,255,255])
    # define range of red color in HSV
    lower_red = np.array([160, 100, 20])
    upper_red = np.array([179, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    #mask = cv.inRange(hsv, lower_red, upper_red)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5 )

    print(bbox)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()