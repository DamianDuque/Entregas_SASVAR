import PySimpleGUI as sg
from datetime import date
import cv2
def main():
    #Conectamos a la webcam
    camaraP = cv2.VideoCapture(0)
    camaraE = cv2.VideoCapture(1)
    #Elegimos un tema de PySimpleGUI
    sg.theme('DarkGreen5')
    #Definimos los elementos de la interfaz grafica
    
    layout1 = [[sg.Image(filename='', key='-image1-')],
              [sg.Button('Tomar Fotografia'),sg.Button('Salir')]]
    
    layout2 = [[sg.Image(filename='', key='-image2-')],
              [sg.Button('Tomar Fotografia'),sg.Button('Salir')]]

    #Creamos la interfaz grafica
    window = sg.Window('Camara portatil',
                       layout1,
                       no_titlebar=False,
                       location=(0, 0))
    image_elem = window['-image1-']
    numero = 0

    window = sg.Window('Camara externa',
                       layout2,
                       no_titlebar=False,
                       location=(0, 0))
    image_elem = window['-image2-']
    numero = 1

    #Iniciamos la lectura y actualizacion
    while (camaraP.isOpened() and camaraE.isOpened):
        #Obtenemos informacion de la interfaz grafica y video
        event, values = window.read(timeout=0)
        ret, frame1 = camaraP.read()

        ret, frame2 = camaraE.read()


        #Si salimos
        if event in ('Exit', None):
            break
        #Si tomamos foto
        elif event == 'Tomar Fotografia':
            ruta = sg.popup_get_folder(title='Guardar Fotografia', message="Carpeta destino")
            cv2.imwrite(ruta + "/" + str(date.today()) + str(numero) + ".png", frame1)
            cv2.imwrite(ruta + "/" + str(date.today()) + str(numero) + ".png", frame2)
        if not ret:
            break
        #Mandamos el video a la GUI
        imgbytes1 = cv2.imencode('.png', frame1)[1].tobytes()  # ditto
        image_elem.update(data=imgbytes1)

        #Mandamos el video a la GUI
        imgbytes2 = cv2.imencode('.png', frame2)[1].tobytes()  # ditto
        image_elem.update(data=imgbytes2)

        numero = numero + 1
main()