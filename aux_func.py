import cv2
import json
import os
from os import mkdir
from datetime import datetime
import time


eCarpeta = os.path.isdir('Observaciones')
nombre_carpeta = "Observaciones"
if eCarpeta == False:
    mkdir(nombre_carpeta)

ruta = os.path.abspath(nombre_carpeta)

print(ruta)


def generarId():
    now = datetime.now()
    dia = format(now.day)
    mes = format(now.month)
    anio = format(now.year)
    hora = format(now.hour)
    minuto = format(now.minute)
    segundo = format(now.second)

    if int(dia) < 10:
        dia = "0" + dia
    if int(mes) < 10:
        mes = "0" + mes
    anio = anio[2:]
    if int(hora) < 10:
        hora = "0" + hora
    if int(minuto) < 10:
        minuto = "0" + minuto
    if int(segundo) < 10:
        segundo = "0" + segundo

    id = dia + mes + anio + hora + minuto + segundo

    return id

def verificar(fotos, CAM_NUM, id, caps, id_etiqueta, dvalue):
    
    print("Porfavor compruebe que el residuo es visible en cada una de las fotos que se tomaron")
    print("Si esto se cumple, presione 'enter', sino, ingrese 'r' para volver a tomar las fotos")
    while True:
        
        for foto in fotos:   
            imagen = cv2.imread(foto)
            cv2.imshow('Fotos', imagen)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        confirmacion = input()
        if confirmacion == "r":
            tomarFotos(CAM_NUM, id, caps, id_etiqueta, dvalue)
        else:
            break
            
        

def tomarFotos(CAM_NUM, id, caps, id_etiqueta, dvalue):
    
    cam = 0
    formFoto = "O_" + str(id_etiqueta) + "_" + str(dvalue) +"_" + str(id)

    nombresFotos = []
    for i in caps:

        os.chdir(ruta)
        cap = cv2.VideoCapture(i)
        ret, frame = cap.read()
        
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")


        print("foto tomada desde la camara: " + str(cam))

        cv2.imwrite(os.path.join(ruta, formFoto + "_" + str(cam) + ".png"), frame)
        cap.release()
        
        nombreFoto = os.path.join(ruta, formFoto + "_" + str(cam) + ".png")
        
        nombresFotos.append(nombreFoto)
        cam = cam + 1

    return nombresFotos

def show_cap(cap, window, scale=1, rect=True, color=(0, 0, 255)):
    """Show video capture in window"""
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=scale, fy=scale)

    # draw square centered on frame
    if rect:
        h, w = frame.shape[:-1]
        # represents the top left corner of rectangle
        halfsize= 10
        start_point = (w//2-halfsize, h//2-halfsize)
        # represents the bottom right corner of rectangle
        end_point = (w//2+halfsize, h//2+halfsize)
        
        # Line thickness of 2 px
        thickness = 1
        
        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        image = cv2.rectangle(frame, start_point, end_point, color, thickness)

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        return
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow(window, frame)

