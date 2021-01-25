import cv2 # activate tf2->pip install opencv-python
import datetime
import os
# 選擇第二隻攝影機->cv2.VideoCapture(1)
# 筆電鏡頭->cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)

c = 0
p = 0
# 讓客戶可以給定記憶體大小，計算最多可以存幾張照片
req = input('Please enter desired memory(unit:MB) : ')
KB = int(req) * 1024
quantity = KB / 9   # 因一張.jpg的大小大約9KB

while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

  # 在圖片上加時間
  now = str(datetime.datetime.now())
  frame = cv2.putText(frame, now, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                           (255, 0, 0), 2, cv2.LINE_AA)

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
    # x = datetime.datetime.now()
    os.makedirs('data', exist_ok=True)
    cv2.imwrite('data/' + str(p) + '.jpg', resized)
    # cv2.imwrite(str(p) + '.png', resized)
    # cv2.imwrite(str(x.year) + '-' + str(x.month) + '-' + str(x.day) + ' ' + str(x.hour) + '-' + str(x.minute) + '-' + str(x.second) + '.jpg', resized)
    if p >= quantity:
      p = 0



  # 若按下 q 鍵則離開迴圈(關閉鏡頭)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()