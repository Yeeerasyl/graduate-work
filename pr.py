from ultralytics import YOLO
import cv2
import re

model = YOLO("best.pt")

im1 = cv2.imread("qqq.jpg")
results = model.predict(source=im1)

final_result = results[0].verbose()

predictions_list = final_result.split(", ")
first_prediction = predictions_list[0]

first_prediction = re.sub(r'[\d\.]+', '', first_prediction)

print(first_prediction)

