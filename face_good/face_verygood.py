from imutils.face_utils import FaceAligner
import dlib
import cv2
import os

input_folder = 'D:\\Face'
output_folder = 'D:\\Face_Ali'


def detect_face_landmarks(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)

    for face in faces:
        facealigned = fa.align(img, gray, face)
        global face_filename
        cv2.imwrite(output_folder + '\\' + f + "_faceAligned.png".format(face_filename), facealigned)
        face_filename += 1


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
fa = FaceAligner(predictor, desiredFaceWidth=200)

face_filename = 1

for root, dirs, files in os.walk(input_folder):
    for f in files:
        filename = root+'\\'+f
        detect_face_landmarks(filename)

print("Done!")
