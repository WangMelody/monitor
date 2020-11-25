import cv2 # activate tf2->pip install opencv-python
import datetime
# 選擇第二隻攝影機->cv2.VideoCapture(1)
# 筆電鏡頭->cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)

c = 0
p = 0
while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()
  width = 160
  height = 120
  dim = (width, height)
  resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

  # rgb -> gray scale
  resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

  # 顯示圖片
  # cv2.imshow('frame', frame)
  # resize image
  cv2.imshow('Resized Image', resized)

  c = c + 1
  if c % 30 == 0:
    p = p + 1
    x = datetime.datetime.now()
    # cv2.imwrite(str(p)+'.jpg', frame)
    cv2.imwrite(str(x.year) + '-' + str(x.month) + '-' + str(x.day) + ' ' + str(x.hour) + '-' + str(x.minute) + '-' + str(x.second) + '.jpg', resized)
    if p >= 60:
      p = 0



  # 若按下 q 鍵則離開迴圈(關閉鏡頭)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()