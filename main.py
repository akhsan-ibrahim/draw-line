import cv2
import numpy as np

prevX,prevY = -1,-1 # default value
def printCoordinate(event, x, y,flags, params):
  global prevX,prevY
  if event == cv2.EVENT_LBUTTONDOWN:
    cv2.circle( # draw circle
      img,
      (x,y), # coordinates cursor point
      3, # radius (large)
      (255,255,255),
      -1 # line thickness
    )

    # set the annotation coordinates clicked
    strXY = '(' + str(x) + ',' + str(y) + ')'
    fontXY = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img,strXY,(x+10,y-10),fontXY,1,(255,255,255))

    # when clicked on two points then draw the line
    if prevX == -1 and prevY == -1:
      prevX,prevY = x,y # store first point
    else:
      cv2.line(img,(prevX,prevY),(x,y),(0,0,255),4)
      prevX,prevY = -1,-1

    cv2.imshow("image", img)

img = np.zeros( # inisisasi array dengan nilai 0
  (700,800,3), # shape (tinggi, lebar, warna RGB)
  dtype=np.uint8
)
cv2.imshow("image", img) # (window name, declared window)

cv2.setMouseCallback("image", printCoordinate) # set callback function when mouse interact with "image" window

cv2.waitKey()
cv2.destroyAllWindows()