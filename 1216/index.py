import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread("./1213/test_image.jpg")

# # BGR을 HSV로
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# lower = np.array([0, 120, 70])  # 빨간색
# upper = np.array([10, 255, 255])

# # 마스크 생성
# mask = cv2.inRange(hsv_image, lower, upper)

# # 원본 이미지에 마스크 적용
# result = cv2.bitwise_and(image, image, mask=mask)

# plt.subplot(1, 3, 1)
# plt.title('original')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.title('mask')
# plt.imshow(mask, cmap='gray')
# plt.axis('off')

# plt.subplot(1, 3, 3)
# plt.title('result')
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.axis('off')

# plt.show()

# cap = cv2.VideoCapture(0)

# if not cap.isOpened:
#     print("웹캠을 열 수 없습니다.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.resize(frame, (640, 480))

#     # hsv로 변경
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # 피부색 범위(hsv)
#     lower = np.array([0, 20, 70])
#     upper = np.array([20, 255, 255])

#     mask = cv2.inRange(hsv, lower, upper)

#     # 노이즈 제거 (모폴로지 연산)
#     mask = cv2.erode(mask, None, iterations=2)
#     mask = cv2.dilate(mask, None, iterations=2)

#     # 컨투어 찾기

#     contours, _ = cv2.findContours(
#         mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # 윤곽선 그리기
#     for con in contours:
#         area = cv2.contourArea(con)

#         cv2.drawContours(frame, [con], -1, (0, 255, 0), 2)

#     cv2.imshow("skin", frame)
#     cv2.imshow("mask", mask)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# haar cascade 불러오기기
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     # 그레이 스케일로 변환
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(
#         gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # 탐지된 얼굴에 사각형 그리기
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#     cv2.imshow('face', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# 눈 인식

# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# eye_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + 'haarcascade_eye.xml')

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("웹캠을 열 수 없습니다.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(
#         gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#         eyes = eye_cascade.detectMultiScale(
#             gray_frame, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))

#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

#         cv2.imshow('eyes', frame)

#         if cv2.waitKey(1) == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# from ultralytics import YOLO

# # YOLO 모델 로드
# model = YOLO('yolov8n.pt')

# # 이미지 로드
# image = cv2.imread("./1216/test.jpg")

# # 예측 수행
# results = model.predict(source=image, save=False, save_txt=False, conf=0.5)

# # 결과를 NumPy 배열로 변환하여 플로팅 이미지 생성
# frame = results[0].plot()  # 괄호 추가하여 메서드 호출

# # 이미지 출력
# cv2.imshow('YOLO', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# OCR

import cv2
import pytesseract

# Tesseract-OCR 실행 파일 경로 설정
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# 이미지 읽기
image = cv2.imread('./1216/car_number.jpg')

# 이미지를 그레이스케일로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_img = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)

# adaptiveThreshold(): 조명에 대응이 쉬움

# Tesseract로 텍스트 추출
text = pytesseract.image_to_string(
    binary_img, lang="eng")

# 추출된 텍스트 출력
print("추출된 텍스트:\n", text)
