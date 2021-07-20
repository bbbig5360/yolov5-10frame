import cv2

def Cut(path_list):
    num=1

    for path in path_list:
        cap = cv2.VideoCapture(path)
        if cap.isOpened() is False:
            print('Error opening video stream or file')
            break
            
        # 전체 프레임 수를 구해서 1개 뺀 것을 frame_index로 넣어서 시작 frame으로 넣어줄 예정.
        frame_index = cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1

        cnt = 1

        fcc = cv2.VideoWriter_fourcc(*'MP4V') 
        width = int(cap.get(3)) 
        height = int(cap.get(4)) 
        out = cv2.VideoWriter('data/cut_videos/'+str(num)+'.mp4', fcc, 20, (width, height))

        while True:
            # 시작하는 frame을 맨 마지막 프레임으로 세팅
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
            ret, frame = cap.read()

            out.write(frame)
            
            # 거꾸로 실행 index 하나씩 빼주기
            frame_index = frame_index-1
            cnt += 1
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

            if cnt > 10 :
                out.release()
                break
        num += 1
        
        cap.release()
        cv2.destroyAllWindows()

