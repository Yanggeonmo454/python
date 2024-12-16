import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


path = "C:\\Windows\\Fonts\\LG_Smart_UI-Light.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

# #path = "C:\\Users\\shg02\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Medium.ttf"
# path = "Pretendard-Medium.ttf"
# font = font_manager.FontProperties(fname=path).get_name()
# plt.rc('font', family=font)

# #이미지 읽기
# image = cv2.imread("./1213/test_image.jpg")

# #opencv BGR -> RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

"""
# cv2.imshow("title", image_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
"""
# plt.figure(figsize=(10, 10))
# #원본
# plt.subplot(2, 2, 1)
# plt.imshow(image_rgb)
# plt.title("원본")
# plt.axis('off')

# ------블러링
# #평균블러
# blurred = cv2.blur(image_rgb, (5, 5))
# plt.subplot(2, 2, 2)
# plt.imshow(blurred)
# plt.title("평균블러")
# plt.axis('off')

# #가우시안블러
# gaussian = cv2.GaussianBlur(image_rgb, (5, 5), 0)
# plt.subplot(2, 2, 3)
# plt.imshow(gaussian)
# plt.title("가우시안블러")
# plt.axis('off')

# #미디언 블러
# median = cv2.medianBlur(image_rgb, 5)
# plt.subplot(2, 2, 4)
# plt.imshow(median)
# plt.title("미디언블러")
# plt.axis('off')

# ----엣지강조
# # 샤프닝 커널
# kernel = np.array([[0, -1, 0],
#                    [-1, 7, -1],
#                    [0, -1, 0] ])
# # 필터 적용
# sharped =  cv2.filter2D(median, -1, kernel)

# plt.subplot(2, 2, 2)
# plt.imshow(sharped)
# plt.title("엣지강조")
# plt.axis('off')


# #----엣지검출
# img = cv2.imread("./1213/test_image.jpg", cv2.IMREAD_GRAYSCALE)
# #img = cv2.imread("./1213/image.png", cv2.IMREAD_GRAYSCALE)

# #sobel
# sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3) #x방향미분
# sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3) #y방향미분
# #CV_32F
# #CV_8U
# sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# #laplacian
# laplacian = cv2.Laplacian(img, cv2.CV_64F)

# #canny
# edges = cv2.Canny(img, 100, 300) #최소값, 최대값

# #원본
# plt.subplot(2, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title('원본')
# plt.axis('off')

# #sobel
# plt.subplot(2, 2, 2)
# plt.imshow(sobel_combined, cmap='gray')
# plt.title('sobel')
# plt.axis('off')

# #laplacian
# plt.subplot(2,2,3)
# plt.imshow(laplacian, cmap='gray')
# plt.title('laplacian')
# plt.axis('off')

# #canny
# plt.subplot(2,2,4)
# plt.imshow(edges, cmap='gray')
# plt.title('canny')
# plt.axis('off')

# --------컨투어
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이스케일로 변환

# #이진화처리
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# #컨투어 감지
# contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# #컨투어 원본에 그리기
# results_img = image.copy()
# cv2.drawContours(results_img, contours, -1, (0, 255, 0), 2)

# plt.subplot(2, 2, 2)
# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
# plt.title("컨투어 그리기")
# plt.axis('off')

# ---------컨투어 계산
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이스케일로 변환
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# results_img = image.copy()

# for contour in contours:
#     # 면적계산
#     #print("면적 : ", cv2.contourArea(contour))

#     # 중심점 계산
#     # M = cv2.moments(contour)
#     # if M['m00'] != 0:   #중심점계산 (m00 = 면적)
#     #     cx = int(M['m10'] / M['m00'] ) #x중심
#     #     cy = int(M['m01'] / M['m00'] ) #y중심

#     #     #중심점표시
#     #     cv2.circle(results_img, (cx, cy), 5, (0, 0, 0), -1)
#     # else:
#     #     print("컨투어 면적이 0")

#     # 둘레 계산
#     print("둘레 : ", cv2.arcLength(contour, True)) #폐곡선 여부

#     cv2.drawContours(results_img, [contour], -1, (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
# plt.show()

# -----------웹캠 연결
cap = cv2.VideoCapture(0)

# codec = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('./1213/output.avi', codec, 20.0, (640, 480))

plt.ion()  # 인터렉티드 모드 : 코드를 실행하면서 창을 표시
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽지 못했습니다")
        break
    # out.write(frame)
    # cv2.imshow("video", frame)
    # 원본

    original = frame.copy()

    # 그레이 스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # gray를 cv2 threshold로 이진화
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 컨투어 탐지
    contours, _ = cv2.findContours(
        binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 컨투어 그리기
    contour_img = frame.copy()

    # 샤프닝 필터
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    # 필터 적용
    sharped = cv2.filter2D(frame, -1, kernel)
    sharped_contour_img = sharped.copy()
    cv2.drawContours(sharped_contour_img, contours, -1, (0, 255, 0), 2)

    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("원본")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
    plt.title("컨투어")
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(sharped_contour_img, cv2.COLOR_BGR2RGB))
    plt.title("샤프닝")
    plt.axis('off')

    plt.pause(0.001)  # 1밀리초동안
    # plt.clf()  # 현재 플롯창에 띄어진것을 초기화

    # 'q' 키로 종료
    key = cv2.waitKey(1)  # 키 입력 대기 (1ms)
    if key == ord('q'):  # 'q' 키가 입력되었는지 확인
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
plt.close()
