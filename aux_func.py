import cv2
import json
import os
from datetime import datetime

nombre_carpeta = "Observaciones"
ruta = os.path.abspath(nombre_carpeta)

print("Cargando camaras y diccionarios...")
with open (os.path.join(ruta, "InfoEtiqueta.json"), 'r') as f:
    diccionarioEtiq = json.load(f)
with open (os.path.join(ruta, "InfoReferencias.json"), 'r') as f:
    diccionarioRef = json.load(f)

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

def tomarFotos(CAM_NUM, id, caps):
    
    cam = 1
    formFoto = "O_" + str(id) + "-"

    for cap in caps:
        ret, frame = cap.read()
        
        if not ret:
            print(print("Can't receive frame (stream end?). Exiting ..."))
        
        cv2.imwrite(os.path.join(ruta, formFoto + str(cam) + ".png") , frame)
        cam = cam + 1

def enumerarOpciones(dic, clave, ids):
    if dic == "1":
        for i, name in enumerate(diccionarioRef[clave].values()):
            _id = ids[i]
            print(f'{_id} - {name}')
    elif dic == "2":
        for i, name in enumerate(diccionarioEtiq[clave].values()):
            _id = ids[i]
            print(f'{_id} - {name}')


def elegir(elemento, ids, dic, caps, SCALE):
    print()
    print("Seleccione " + elemento + " a traves del caracter marcado al costado izquierdo")
    if dic == "Ref":
        enumerarOpciones("1", elemento, ids)
    else:
        enumerarOpciones("2", elemento, ids)

    while True:
        i=0
        for cap in caps:
            show_cap(cap, f'cam-{i}', scale=SCALE)
            i+=1
 
        key = cv2.waitKey(1)

        for k in ids:
            if key == ord(k):
                if dic != "Ref":
                    eleccion = diccionarioEtiq[elemento][k]
                else:
                    eleccion = diccionarioRef[elemento][k]
                cv2.destroyAllWindows()
                return eleccion


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

