- YOLOv5 기법을 이용해 사람만 검출하는 인공지능 모델을 만들었습니다.

시나리오 : 
각 기관에서는 CCTV를 이용해 데이터를 저장하는데, 저장된 영상데이터를 이용해 해당 위치의 인구수를 파악합니다.
일정 시간마다 마지막 영상의 10프레임(또는 원하는 만큼)의 데이터를 가져와 인구수 검출 후 평균을 내어 오차를 최소화합니다.

- 해당 모델은 약 2000장의 이미지를 Bounding Box하여 학습 데이터셋을 만들었습니다.
  이유 : YOLO특성상 작은 사람과 겹친 사람을 검출하지 못해서입니다.
  
- 해당 소스를 제공받았을 때 하나의 동영상(또는 이미지)을 디텍팅했습니다.
  -> 7개의 영상을 순서대로 처리해 동시에 처리하는것처럼 만들었습니다.( i5-4690 cpu만을 사용해 20초 이내에 작업이 종료됩니다. )



