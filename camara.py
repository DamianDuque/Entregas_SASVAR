import cv2

CAM_NUM = 1
SCALE = 0.5
 
print("Iniciando camara")
cap = cv2.VideoCapture(3)

if not cap.isOpened():
    print("Cannot open camera")


while True:
    ret, frame = cap.read()
    if not ret :
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('Imagen1', frame)

    key = cv2.waitKey(1)
    if key == ord("a"):
        cv2.destroyAllWindows()