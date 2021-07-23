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

video_cnt = 2
flag = video_cnt+1

while True :
    if flag != 0:
        out1 = cv2.VideoWriter('data/cut_videos/1.mp4', fourcc, 20.0, (640,480))
        out2 = cv2.VideoWriter('data/cut_videos/2.mp4', fourcc, 20.0, (640,480))

    cnt = 0
    flag = 0

    # 몇초에 한 번 실행할지 설정.
    if (int(time.time()) - start_t)%60 == 0:
        while_flag = True

    while while_flag:
        if flag%2 == 0:
            ret, frame = cap1.read()
        else :
            ret, frame = cap2.read()

        cnt += 1
        if cnt%10 == 0:
            flag += 1

        if flag == 1:
            out1.write(frame)            
        elif flag == 2:
            if cnt%10 == 0:
                out1.release()
            out2.write(frame)
        elif flag > 2:
            if cnt%10 == 0:
                out2.release()
            yolo_start()
            cv2.destroyAllWindows()

            while_flag = False
            cnt = 0

    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
        break


cap1.release()
cap2.release()
cv2.destroyAllWindows()