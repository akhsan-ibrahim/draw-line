import cv2
import numpy as np

def printCoordinate(event, x, y,flags, params):
  if event == cv2.EVENT_LBUTTONDOWN:
    cv2.circle( # draw circle
      img,
      (x,y), # coordinates cursor point
      3, # radius (large)
      (255,255,255),
      -1 # line thickness
    )
    strXY = '(' + str(x) + ',' + str(y) + ')'
    fontXY = cv2.FONT_HERSHEY_PLAIN

    cv2.putText(img,strXY,(x+10,y-10),fontXY,1,(255,255,255))
    cv2.imshow("image", img)

img = np.zeros( # inisisasi array dengan nilai 0
  (700,800,3), # shape (tinggi, lebar, warna RGB)
  dtype=np.uint8
)
cv2.imshow("image", img) # (window name, declared window)

cv2.setMouseCallback("image", printCoordinate) # set callback function when mouse interact with "image" window

cv2.waitKey()
cv2.destroyAllWindows()