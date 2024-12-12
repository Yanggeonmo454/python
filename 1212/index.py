import cv2
import numpy as np
# # 이미지 파일 경로
# image_color = cv2.imread("./1212/image.png")

# # scale = 0.5
# # resized = cv2.resize(image_color, None, fx=scale, fy=scale)
# roi = image_color[50:300, 100:300].copy()

# x,y 값 찾기
# def mouse_click(e, x, y, flag, param):
#     if e == cv2.EVENT_LBUTTONDOWN:
#         print(f"마우스 위치: x={x}, y ={y}")


# image_color = cv2.imread("./1212/image.png")
# cv2.imshow("image", image_color)

# # 마우스 콜백 함수
# cv2.setMouseCallback("image", mouse_click)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# roi만 표시

# start = None
# end = None


# def mouse_select(e, x, y, flag, param):
#     global start, end
#     if e == cv2.EVENT_LBUTTONDOWN:
#         start = (x, y)
#     elif e == cv2.EVENT_LBUTTONUP:
#         end = (x, y)

#         # 선택된 영역을 잘라서 표시
#         roi = image_color[start[1]:end[1], start[0]:end[0]]
#         cv2.imshow("select", roi)


# # 이미지 읽기
# image_color = cv2.imread("./1212/image.png")
# cv2.imshow("image", image_color)

# # 마우스 콜백 함수 설정
# cv2.setMouseCallback("image", mouse_select)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import numpy as np


# image_color = cv2.imread("./1212/image.png")

# (h, w) = image_color[:2]
# center = (w//2, h//2)

# matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
# rotated = cv2.warpAffine(image_color, matrix, (w, h))

# cv2.imshow("image", rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


image_color = cv2.imread("./1212/image.png")
cv2.imshow("image_color", image_color)

gray_image = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_image)

scale = 0.5
resized_image = cv2.resize(image_color, (0, 0), fx=scale, fy=scale)
cv2.imshow("resized image", resized_image)

(h, w) = image_color.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image_color, matrix, (w, h))

cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
