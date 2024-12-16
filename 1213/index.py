import cv2
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

# 한글 폰트 설정
path = "C:\\Windows\\Fonts\\LG_Smart_UI-Light.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

# 이미지 읽기 및 RGB 변환
image = cv2.imread("./1213/test_image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# OpenCV로 원본 이미지 표시
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Matplotlib로 이미지 비교
# plt.figure(figsize=(10, 10))

# # 원본 이미지
# plt.subplot(2, 2, 1)
# plt.imshow(image_rgb)
# plt.axis('off')
# plt.title("원본")

# # 평균 블러
# blurred = cv2.blur(image_rgb, (3, 3))
# plt.subplot(2, 2, 2)
# plt.imshow(blurred)
# plt.axis('off')
# plt.title("평균 블러")

# # 가우시안 블러
# gaussian = cv2.GaussianBlur(image_rgb, (5, 5), 0)
# plt.subplot(2, 2, 3)
# plt.imshow(gaussian)
# plt.axis('off')
# plt.title("가우시안 블러")

# # 미디안 블러
# median = cv2.medianBlur(image_rgb, 5)
# plt.subplot(2, 2, 4)
# plt.imshow(median)
# plt.axis('off')
# plt.title("미디안 블러")

# # 결과 출력
# plt.show()

# kernel = np.array([[0, -1, 0],
#                   [-1, 5, -1],
#                   [0, -1, 0]])

# sharped = cv2.filter2D(image_rgb, -1, kernel)
# plt.subplot(2, 2, 2)
# plt.imshow(sharped)
# plt.axis("off")

img = cv2.imread("./1213/test_image.jpg", cv2.IMREAD_GRAYSCALE)

# sobel
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# 원본
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("원본")
plt.axis('off')

# sobel
plt.subplot(2, 2, 2)
plt.imshow(sobel_combined, cmap='gray')
plt.title('sobel')
plt.axis('off')


# laplacian

# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# plt.subplot(2, 2, 3)
# plt.imshow(laplacian, cmap='gray')
# plt.title('laplacian')
# plt.axis('off')

# # canny
# edges = cv2.Canny(img, 100, 500)

# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# plt.subplot(2, 2, 4)
# plt.imshow(edges, cmap='gray')
# plt.title('laplacian')
# plt.axis('off')


# plt.show()

# 컨투어
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # 이진화 처리리
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# # 컨투어 감지
# contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # 컨투어 원본에 그리기
# results_img = image.copy()
# cv2.drawContours(results_img, contours, -1, (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
# plt.title("컨투어 그리기")
# plt.axis("off")

# 컨투어 계산
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# results_img = image.copy()

# for contour in contours:
#     # 면적 계산 부분은 주석 처리
#     # print("면적: ", cv2.contourArea(contour))

#     M = cv2.moments(contour)
#     if M['m00'] != 0:  # 중심점 계산
#         cx = int(M['m10']/M['m00'])  # x중심
#         cy = int(M['m01']/M['m00'])  # y중심

#         cv2.circle(results_img, (cx, cy), 5, (0, 0, 255), -1)  # 중심점 그리기
#     else:
#         print("컨투어 면적이 0")

#     # 각 컨투어를 그리기
#     cv2.drawContours(results_img, [contour], -1, (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
# plt.show()

# # 둘레 계산

# print(cv2.arcLength(contour, True))

# cv2.drawContours(results_img, [contour], -1, (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
# plt.show()


# 웹캠 연결

cap = cv2.VideoCapture(0)

# codec = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', codec, 20.0, (640, 480))

plt.ion()  # 인터렉티드 모드 : 코드를 실행하면서 창을 표시
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    original = frame.copy()

    gaussian = cv2. GaussianBlur(frame, (5, 5), 0)

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("원본")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
    cv2.imshow("video", frame)
    plt.title("가우시안 블러")
    plt.axis('off')

    plt.pause(0.001)
    plt.clf()

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
plt.close()
