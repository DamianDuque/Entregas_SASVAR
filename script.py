from datetime import datetime
import os
from os import mkdir
import cv2
import keyboard

print("Presione Espacio o Enter para tomas fotos")

while True:

    now = datetime.now()
    dia = format(now.day)
    mes = format(now.month)
    anio = format(now.year)
    hora = format(now.hour)
    minuto = format(now.minute)
    segundo = format(now.second)
    
    if keyboard.is_pressed('e'):
            break

    if keyboard.is_pressed('space') or keyboard.is_pressed('enter'):
        
        if int(dia) < 10:
            dia = '0' + dia

        if int(mes) < 10:
            mes = '0' + mes

        anio = anio[2:]

        if int(hora) < 10:
            hora = '0' + hora

        if int(minuto) < 10:
            minuto = '0' + minuto

        if int(segundo) < 10:
            segundo = '0' + segundo


        print("Tomando fotos")


        id = dia + mes + anio + hora + minuto + segundo

        archivo = 'O_'
        nombre_carpeta = archivo + str(id)
        
        mkdir(nombre_carpeta)
        
        ruta = os.path.abspath(nombre_carpeta)

        cap = cv2.VideoCapture(0)
        leido, frame = cap.read()
        cap2 = cv2.VideoCapture(1)
        leido2, frame2 = cap2.read()
        if (leido == True) and (leido2 == True):

            cv2.imwrite(os.path.join(ruta, "foto1.png") , frame)
            cv2.imwrite(os.path.join(ruta, "foto2.png") , frame2)

            print("Fotos tomadas correctamente")

        else:
            print("Error al acceder a las cámaras")

        cap.release()
        cap2.release()

        