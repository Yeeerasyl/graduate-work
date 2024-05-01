from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("best.pt")

im1 = cv2.imread("www.jpg")
results = model.predict(source=im1) 
