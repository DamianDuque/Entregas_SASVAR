import cv2
import os

import aux_func as au

#Inicializar etiqueta
damage = "N/A"

nombre_carpeta = "Observaciones"
ruta = os.path.abspath(nombre_carpeta)

# Number of cameras to display
CAM_NUM = 3
SCALE = 0.5

def nuevoResiduo(caps, ):
    while True:
        print("Porfavor ingrese el id de la etiqueta del residuo a fotografiar")
        id_etiqueta = input()

        print("Porfavor ingrese el numero correspondiente al estado del residuo:")
        print("0 - Intacto")
        print("1 - Medio")
        print("2 - Dañado")

        dvalue = 1 #input()

        print("Ingrese x para tomar fotos o e para salir")
        ing = input()

        if ing == "e":
            exit()

        if ing == "x":
            print("Tomando fotos")
            id = au.generarId()
            fotos = au.tomarFotos(CAM_NUM, id, caps, id_etiqueta, dvalue)

        print(fotos)
        au.verificar(fotos, CAM_NUM, id, caps, id_etiqueta, dvalue)

        print("Ingrese n si desea etiquetar un nuevo reisudo, enter si desea continuar con el mismo residuo")
        reuse = input()
        if reuse == "n":
            continue

        else:
            mismoResiduo(caps, id_etiqueta)


def mismoResiduo(caps, id_etiqueta):
    while True:
        print("Porfavor ingrese el numero correspondiente al estado del residuo:")
        print("0 - Intacto")
        print("1 - Medio")
        print("2 - Dañado")

        dvalue = 1 #input()

        print("Ingrese x para tomar fotos o e para salir")
        ing = input()

        if ing == "e":
            exit()

        if ing == "x":
            print("Tomando fotos")
            id = au.generarId()
            fotos = au.tomarFotos(CAM_NUM, id, caps, id_etiqueta, dvalue)

        print(fotos)
        au.verificar(fotos, CAM_NUM, id, caps, id_etiqueta, dvalue)


        print("Ingrese n si desea etiquetar un nuevo reisudo, enter si desea continuar con el mismo residuo")
        reuse = input()
        if reuse == "n":
            nuevoResiduo(caps)

        else:
            mismoResiduo(caps, id_etiqueta)


def main():
    #caps = [cv2.VideoCapture(i) for i in range(CAM_NUM) if cv2.VideoCapture(i).isOpened and i != 3]
    #print(caps)
    caps = [0,1]
    
    while True:
        print("Porfavor ingrese el id de la etiqueta del residuo a fotografiar")
        id_etiqueta = input()

        print("Porfavor ingrese el numero correspondiente al estado del residuo:")
        print("0 - Intacto")
        print("1 - Medio")
        print("2 - Dañado")

        dvalue = 1 #input()

        print("Ingrese x para tomar fotos o e para salir")
        ing = input()

        if ing == "e":
            exit()

        if ing == "x":
            print("Tomando fotos")
            id = au.generarId()
            fotos = au.tomarFotos(CAM_NUM, id, caps, id_etiqueta, dvalue)

        print(fotos)
        au.verificar(fotos, CAM_NUM, id, caps, id_etiqueta, dvalue)

        print("Ingrese n si desea etiquetar un nuevo reisudo, enter si desea continuar con el mismo residuo")
        reuse = input()
        if reuse == "n":
            nuevoResiduo(caps)

        else:
            mismoResiduo(caps, id_etiqueta)

if __name__ == '__main__':
    main()
