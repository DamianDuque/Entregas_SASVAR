import os
from os import mkdir
import cv2
import keyboard

id = 0

while True:
    
    if keyboard.is_pressed('e'):
            break

    if keyboard.is_pressed('space') or keyboard.is_pressed('enter'):
        
        print("Tomando fotos")

        archivo = 'observacion_'
        nombre_carpeta = archivo + str(id)

        mkdir(nombre_carpeta)        
        id = id + 1
        
        ruta = os.path.abspath(nombre_carpeta)

        cap = cv2.VideoCapture(0)
        leido, frame = cap.read()
        cap2 = cv2.VideoCapture(1)
        leido2, frame2 = cap2.read()
        if (leido == True) and (leido2 == True):

            cv2.imwrite(ruta + "/" + "foto1.png" , frame)
            cv2.imwrite(ruta + "/" + "foto2.png" , frame2)

            print("Fotos tomadas correctamente")

        else:
            print("Error al acceder a las cámaras")

        cap.release()
        cap2.release()

        