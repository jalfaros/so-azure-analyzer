import cv2
import math
import os
from os import mkdir
import time


def videoProcessor( videoPathFile ):
    print("Processing the video...")
    count =  0
    cap = cv2.VideoCapture( videoPathFile )
    frameRate = cap.get(5)
    video_path_save = './video_images/' + videoPathFile.split("/")[-1][0:-4]
    video_file_name = videoPathFile.split("/")[-1][0:-4]

    if not ( os.path.isdir( video_path_save ) ):
        os.mkdir( video_path_save )

    
    while( cap.isOpened() ):

        if ( count != 30 ):
            
            frameId = cap.get(1)
            ret, frame = cap.read()

            if not ret:
                break
            if( frameId % math.floor(frameRate) == 0 ):
                image_filename = video_path_save + '/' + video_file_name + "%d.jpg" % count
                cv2.imwrite( image_filename, frame )
                count += 1
        else:
            break

    cap.release()
    print("Video processed")
videoProcessor('./videos/shot_at_the_night.mp4')