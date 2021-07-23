import cv2
import time
from cam_detect import yolo_start
import os 

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

ret,frame = cap1.read()

fourcc = cv2.VideoWriter_fourcc(*'MP4V')

start_t = int(time.time())

while_flag = False
flag = 8

while True :
    if flag != 0:
        out1 = cv2.VideoWriter('data/cut_videos/1.mp4', fourcc, 20.0, (640,480))
        out2 = cv2.VideoWriter('data/cut_videos/2.mp4', fourcc, 20.0, (640,480))
        out3 = cv2.VideoWriter('data/cut_videos/3.mp4', fourcc, 20.0, (640,480))
        out4 = cv2.VideoWriter('data/cut_videos/4.mp4', fourcc, 20.0, (640,480))
        out5 = cv2.VideoWriter('data/cut_videos/5.mp4', fourcc, 20.0, (640,480))
        out6 = cv2.VideoWriter('data/cut_videos/6.mp4', fourcc, 20.0, (640,480))
        out7 = cv2.VideoWriter('data/cut_videos/7.mp4', fourcc, 20.0, (640,480))

    cnt = 0
    flag = 0

    if (int(time.time()) - start_t)%300 == 0:
        while_flag = True

    while while_flag:
        if flag%2 == 0:
            ret, frame = cap1.read()
        else :
            ret, frame = cap2.read()

        cnt += 1
        cv2.imshow('cam'+str(flag), frame)

        if cnt%10 == 0:
            flag += 1

        if flag == 1:
            out1.write(frame)            
        elif flag == 2:
            if cnt%10 == 0:
                out1.release()
            out2.write(frame)
        elif flag == 3:
            if cnt%10 == 0:
                out2.release()
            out3.write(frame)
        elif flag == 4:
            if cnt%10 == 0:
                out3.release()
            out4.write(frame)
        elif flag == 5:
            if cnt%10 == 0:
                out4.release()
            out5.write(frame)
        elif flag == 6:
            if cnt%10 == 0:
                out5.release()
            out6.write(frame)
        elif flag == 7:
            if cnt%10 == 0:
                out6.release()
            out7.write(frame)
        elif flag > 7:
            if cnt%10 == 0:
                out7.release()
            yolo_start()
            cv2.destroyAllWindows()
            for i in range(7):
                os.remove('data/cut_videos/'+str(i+1)+'.mp4')
            while_flag = False

    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
        break


cap1.release()
cap2.release()
cv2.destroyAllWindows()