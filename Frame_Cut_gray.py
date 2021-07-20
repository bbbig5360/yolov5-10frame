import cv2

def Cut(path_list):
    num=1

    for path in path_list:
        cap = cv2.VideoCapture(path)
        print(path)
        if cap.isOpened() is False:
            print('Error opening video stream or file')
            
        # 전체 프레임 수를 구해서 1개 뺀 것을 frame_index로 넣어서 시작 frame으로 넣어줄 예정.
        frame_index = cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1

        cnt = 1

        fcc = cv2.VideoWriter_fourcc(*'MP4V') 
        width = int(cap.get(3)) 
        height = int(cap.get(4)) 
        out = cv2.VideoWriter('data/cut_videos/'+str(num)+'.mp4', fcc, 20, (width, height),0)

        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            out.write(gray)
            
            frame_index = frame_index-1
            cnt += 1

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

            if cnt > 10 :
                break
        num += 1

        cap.release()
        cv2.destroyAllWindows()