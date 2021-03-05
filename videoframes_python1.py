# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:23:51 2021

@author: jacob
"""

# Python program to play a video 
# in reverse mode using opencv  
  
# import cv2 library 
import cv2 
  
# videoCapture method of cv2 return video object 
  
# Pass absolute address of video file  
cap = cv2.VideoCapture("penal.mp4") 
tot_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# read method of video object will return 
# a tuple with 1st element denotes whether 
# the frame was read successfully or not, 
# 2nd element is the actual frame. 
  
# Grab the current frame. 
check , vid = cap.read() 
  
# counter variable for 
# counting frames 
counter = 0
  
# Initialize the value 
# of check variable 
check = True
  
frame_list = [] 
  
# If reached the end of the video  
# then we got False value of check. 
  
# keep looping untill we 
# got False value of check. 
while(check == True): 
      
    # imwrite method of cv2 saves the  
    # image to the specified format. 
    #cv2.imwrite("frame%d.jpg" %counter , vid) 
    check , vid = cap.read() 
      
    # Add each frame in the list by 
    # using append method of the List 
    frame_list.append(vid) 
      
  
# last value in the frame_list is None 
# because when video reaches to the end 
# then false value store in check variable 
# and None value is store in vide variable. 
  
# removing the last value from the  
# frame_list by using pop method of List 
frame_list.pop() 
print(len(frame_list))
frame_num = 0  
while frame_num < tot_frames:
    cv2.imshow("Frame",frame_list[frame_num])
    
    key = cv2.waitKey(0)
    
    while key not in [ord('q'), ord('l'), ord("j")]:
        key = cv2.waitKey(0)
    if key == ord("l"):
            frame_num += 1
    if key == ord("j") and frame_num != 0:
            frame_num -= 1
    # Quit when 'q' is pressed
    if key == ord('q'):
            break

"""# looping in the List of frames. 
for frame in frame_list: 
      
    # show the frame. 
    cv2.imshow("Frame" , frame) 
      
    # waitkey method to stoping the frame 
    # for some time. q key is presses, 
    # stop the loop 
    if cv2.waitKey(25) and 0xFF == ord("q"): 
        break
      
# release method of video  
# object clean the input video 
cap.release() 
  
# close any open windows 
cv2.destroyAllWindows() 
  
# reverse the order of the element  
# present in the list by using 
# reverse method of the List. 
frame_list.reverse() 
  
for frame in frame_list: 
    cv2.imshow("Frame" , frame) 
    if cv2.waitKey(25) and 0xFF == ord("q"): 
        break
""" 
cap.release() 
cv2.destroyAllWindows() 