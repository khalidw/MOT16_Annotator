import cv2, numpy as np
import argparse
import os

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-l", "--location", required=True,
   help="Path of the input video")
args = vars(ap.parse_args())

# Click on one corner of the image,
# then, click on the other corner on the image.
# The coordinates will be saved in det/det.txt

# Press 'esc' to quit
# Press 'n' for next frame

# Before you begin, change the path to you own video:
cap = cv2.VideoCapture(args['location'])

# Create a folder "det" for the detections in the same location as input video:
path_to_detection_folder, _ = os.path.split(args['location'])
new_path = os.path.join(path_to_detection_folder, 'det')

if not os.path.exists(new_path):
  os.mkdir(new_path)


#mouse callback function
global click_list
global positions
positions, click_list = [], []

def callback(event, x, y, flags, param):
    if event == 1: click_list.append((x,y))
    positions.append((x,y))    
    
cv2.namedWindow('img')
cv2.setMouseCallback('img', callback)
image_number = 0

frame_number = 1

#read first image
ret, img_p = cap.read()

# get width and height of the original frame
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# calculate resize factor, this will be used to correct the bounding boxes
# as we are drawing them on a resized scale
rf_w = w/1280 # original fame width / rescaled width
rf_h = h/720 # original fame height / rescaled height

img_p = cv2.resize(img_p, (1280,720))

with open('%s/det.txt'%(new_path),'w') as out_file:
  while (cap.isOpened()):

    img = img_p.copy()

    if len(click_list)>0:

      mouse_position = positions[-1]

      a = click_list[-1][0], click_list[-1][1]
      b = mouse_position[0], click_list[-1][1]
      cv2.line(img, a, b, (123,234,123), 3)

      a = click_list[-1][0], mouse_position[1]
      b = mouse_position[0], mouse_position[1]
      cv2.line(img, a, b, (123,234,123), 3)

      a = mouse_position[0], click_list[-1][1]
      b = mouse_position[0], mouse_position[1]
      cv2.line(img, a, b, (123,234,123), 3)

      a = click_list[-1][0], mouse_position[1]
      b = click_list[-1][0], click_list[-1][1]
      cv2.line(img, a, b, (123,234,123), 3)


    # If there are four points in the click list, save the image
    if len(click_list) == 2:

      #get the top left and bottom right
      a,b  = click_list

      #with open('%s/det.txt'%(new_path),'w') as out_file:
      # MOT 16 det,tx format
      # frame id, -1, xmin, ymin, width, height, confidence, -1, -1, -1
      # as our detections are manual, we will set confidence score as 1
      xmin = min(a[0],b[0])*rf_w
      ymin = min(a[1],b[1])*rf_h
      xmax = max(a[0],b[0])*rf_w
      ymax = max(a[1],b[1])*rf_h
      width = xmax-xmin
      height = ymax-ymin
      print('%d,-1,%.2f,%.2f,%.2f,%.2f,1,-1,-1,-1'%(frame_number,xmin,ymin,width,height),file=out_file)
      print(f"{frame_number}, -1, {xmin}, {ymin}, {width}, {height}, 1, -1, -1, -1")

      #reset the click list
      click_list = []

    # show the image and wait
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
    # escape if 'esc' is pressed
    # 27 is the ascii code for 'esc'
    if k == 27: break

    # read next image if 'n' is pressed
    # 110 is the ascii code for 'n'
    if k == 110:
      ret, img = cap.read()
      frame_number += 1
      if not ret:
        break
      img_p = cv2.resize(img, (1280,720))

cap.release()
cv2.destroyAllWindows()