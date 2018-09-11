import cv2
import numpy as np
import datetime
from PIL import Image, ImageDraw
 
def getThisDone(frame):
	# print("Hello from a function 2")
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	return gray
 
def get_colors(infile, numcolors=10, swatchsize=180, resize=150):
    image = Image.fromarray(infile)
    image = image.resize((resize, resize))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize*resize)
    # Save colors to file

    colors.sort(reverse=True)
    # return colors
    sum = 0
    for i in colors:
        sum += i[0]
    # print(sum)
    pal = Image.new('RGB', (swatchsize*8, swatchsize))
    draw = ImageDraw.Draw(pal)

    posx = 0
    for count, col in colors:
        per = count*100/sum	
        # print(per/swatchsize)
        draw.rectangle([posx, 0, posx+(per*8*swatchsize/100), swatchsize], fill=col)
        posx = posx + (per*8*swatchsize/100)
    del draw
    return pal

 
# Create a VideoCapture object
cap = cv2.VideoCapture('video1.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outpy.avi',fourcc, fps, (1920,1080))
 
frame_num = 0
output = np.ones((150,1200,3), np.uint8)
while(True):
  ret, frame = cap.read()
  
  if ret == True: 
    # Create a black image
    blank = np.ones((1080,1920,3), np.uint8)
    blank *= 255

    frame = frame[150:920, 0:1920]
	
    # blank[0:820, 0:1920] = frame
    blank[0:770, 0:1920] = frame
    
    # if frame_num%24 == 0:
    #     cv2.imshow('frame',blank)
    #     cv2.waitKey(5000)
    # frame2 = getThisDone(frame)
	# Write the frame into the file 'output.avi'
    file_name = str(datetime.datetime.now().time()) + ".png"
    # print(np.flip(frame[0],1))
    # get_colors(np.flip(frame), "./export/" + file_name[-13:])
    if frame_num%12 == 0:
        print(frame_num)
        output = get_colors(frame)
    
    blank[820:1000, 240:1680] = output
    
    # if frame_num%15 == 0:
	    # print(frame_num)
        # cv2.imshow('frame',blank)
        # cv2.waitKey(5000)
    out.write(blank)
    # Display the resulting frame    
    
    frame_num += 1
	
    #  if frame_num%100 == 0:
	#     break
    # break
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows() 
