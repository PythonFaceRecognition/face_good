import dlib
import cv2
import os

input_folder = 'D:\\CBSR_database\\test_release\\test_release'
output_folder = 'D:\\Face'

count = 0

for root, dirs, files in os.walk(input_folder):
    for f in files:

        cap = cv2.VideoCapture(root+"\\"+f)   # 開啟影片檔案

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    # 取得畫面尺寸

        detector = dlib.get_frontal_face_detector()  # Dlib的人臉偵測器

        face_filename = 1

        cap.read()
        last_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        frame_counter = 1

        while cap.isOpened() and frame_counter < last_frame:   # 以迴圈從影片檔案讀取影格，並顯示出來
            ret, frame = cap.read()

        # 偵測人臉
            face_rects, scores, idx = detector.run(frame, 0)

            # 取出所有偵測的結果
            for i, d in enumerate(face_rects):

                x1 = d.left()
                y1 = d.top()
                x2 = d.right()
                y2 = d.bottom()
                # 以方框標示偵測的人臉

                crop_img = frame[y1-100:y2+100, x1-100:x2+100]
                cv2.imwrite(output_folder + '\\' + f + "_{0}.png".format(face_filename), crop_img)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)

                face_filename += 1
                frame_counter += 1

                cv2.imshow('Face Detection', frame)  # 顯示結果

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
