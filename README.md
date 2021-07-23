시나리오 : 
각 기관에서는 CCTV를 이용해 데이터를 저장하는데, 저장된 영상데이터를 이용해 해당 위치의 인구수를 파악합니다.
일정 시간마다 마지막 영상의 10프레임(또는 원하는 만큼)의 데이터를 가져와 인구수 검출 후 평균을 내어 오차를 최소화합니다.


- YOLOv5 기법을 이용해 사람만 검출하는 인공지능 모델을 만들었습니다.

- 해당 모델은 1500장 이상의 이미지를 Bounding Box하여 학습 데이터셋을 만들었습니다.
  이유 : YOLO특성상 작은 사람과 겹친 사람을 검출하지 못해서입니다.
  
- 해당 소스를 제공받았을 때 하나의 동영상(또는 이미지)을 디텍팅했습니다.
  -> 7개의 영상을 순서대로 처리해 동시에 처리하는것처럼 만들었습니다.( i5-4690 cpu만을 사용해 20초 이내에 작업이 종료됩니다. )

data폴더의 videos에 7개의 영상데이터가 저장되어있고, 해당 영상을 읽어 마지막 10프레임만 가져옵니다.
cut_videos에 10프레임의 영상 7개가 저장되면 학습된 모델을 이용해 각 영상에서 사람을 디텍팅합니다.

10프레임의 영상을 모두 읽어서 나온 인구수를 평균을 내어 저장합니다.
각 영상의 평균 인구수를 구해 DB에 업데이트합니다.( 이 부분은 제 DB정보가 들어가있어 올리지 않았습니다. )

야간의 상황에는 IR카메라를 쓴다는 가정을 하여 gray이미지로도 바꾸어 인구수를 검출할 수 있도록 코드를 추가하였습니다.(Frame_Cut_gray.py)


실행 방법: 원하는 영상7개를 data/videos에 저장 후 detect.py를 실행하면 됩니다.
          
          
추가 : usb cam 2개를 이용해 일정시간(60초)마다 10프레임을 받아와 평균 인구수를 추출합니다.(2개의 카메라 영상을 저장 후 분석을 마칠때까지 약 6초의 시간이 걸립니다.)
      
      여러대의 네트워크 카메라를 연결해 사용한다면 i5 4690 CPU를 사용할 때, 15대의 카메라 영상을 1분마다 업데이트 가능합니다. GPU연결시 더 높은 성능을 보여줍니다.
실행 방법 : 2cam.py 실행합니다.
