from ultralytics import YOLO
import cv2
import csv
import torch
import numpy as np
import matplotlib.pyplot as plt

model = YOLO('yolov8n-pose.pt')

video_path = "./A11.mp4"

capture = cv2.VideoCapture(video_path)
capture.set(cv2.CAP_PROP_FPS, 10)

with open('test.csv', 'a', newline='') as csvfile:
    write = csv.writer(csvfile)


    while capture.isOpened():
        success, frame = capture.read()
        if success:
            # 推論を実行
            results = model(frame)

            annotatedFrame = results[0].plot()
            cv2.imshow("YOLOv8 Inference", annotatedFrame)

            # 検出オブジェクトの名前、バウンディングボックス座標を取得
            names = results[0].names
            classes = results[0].boxes.cls
            boxes = results[0].boxes

            for box, cls in zip(boxes, classes):
                name = names[int(cls)]
                x1, y1, x2, y2 = [int(i) for i in box.xyxy[0]]

            if len(results[0].keypoints) == 0:
                continue

            # 姿勢分析結果のキーポイントを取得する
            keypoints = results[0].keypoints
            for keypoint in keypoints[0]:
                print(keypoint[0].xy)
                write.writerow(keypoint[0].xy)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

file_path = 'test.csv'
matrix_data = np.genfromtxt(file_path, delimiter=',')

def plot_tensor(tensor):
    fig, ax = plt.subplots()
    cax = ax.matshow(tensor, cmap='viridis')
    fig.colorbox(cax)
    plt.show()

plot_tensor(matrix_data)

capture.release()
cv2.destroyAllWindows()