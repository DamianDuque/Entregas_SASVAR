from datetime import datetime
import PySimpleGUI as sg
import aux_func as au
from os import mkdir
import cv2
import os
import json

#Inicializar etiqueta
material = "N/A"
package_color = "N/A"
packaging_type = "N/A"
capacity = "N/A"
bottle_cap = "N/A"
dirtiness = "N/A"
damage = "N/A"
brand = "N/A"
reference = "N/A"

nombre_carpeta = "Observaciones"
ruta = os.path.abspath(nombre_carpeta)

# Number of cameras to display
CAM_NUM = 2
SCALE = 0.5

def mismoResiduo(caps, valid_id, ma, co, em, ca, tb, su, mar, ref):
    while True:
        print("Ingrese x para tomar fotos o e para salir")
        ing = input()

        if ing == "e":
            exit()

        if ing == "x":
            print("Tomando fotos")
            id = au.generarId()
            au.tomarFotos(CAM_NUM, id, caps)

        damage = au.elegir("Dano", valid_id, "Etiq", caps, SCALE)

        Etiqueta = {
            "Material": ma,
            "Package color" : co,
            "Packaging type": em,
            "Capacity": ca,
            "Bottle cap": tb,
            "Dirtiness": su,
            "Damage": damage,
            "Brand": mar,
            "Reference": ref,
        }
        
        with open (os.path.join(ruta, "O_" + id + '.json'), 'w') as f:
            json.dump(Etiqueta, f)

def main():

    caps = [cv2.VideoCapture(i) for i in range(CAM_NUM) if cv2.VideoCapture(i).isOpened]
    
    print("Ingrese x para tomar fotos o e para salir")
    ing = input()

    if ing == "e":
        exit()

    if ing == "x":
        print("Tomando fotos")
        id = au.generarId()
        au.tomarFotos(CAM_NUM, id , caps)

    valid_id = ['0', '1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    while True:
        print("Iniciando proceso de etiquetado, ingrese e para salir o presione enter para continuar")

        a = input()
        if a == "e":
            exit()

        material = au.elegir("Material", valid_id, "Etiq", caps,  SCALE)

        if material == "PET" or material == "PE-HD" or material == "PVC" or material == "PE-LD" or material == "PP" or material == "PS" or material == "Other plastic" or material == "Glass":
            package_color = au.elegir("Color", valid_id, "Etiq", caps, SCALE)
            
        packaging_type = au.elegir("tipo de empaque", valid_id, "Etiq", caps, SCALE)

        if packaging_type == "Bottle" or packaging_type == "Can" or packaging_type == "Box" or packaging_type == "Other":
            capacity = au.elegir("Capacidad", valid_id, "Etiq", caps, SCALE)

        if packaging_type == "Bottle" or packaging_type == "Cup":
            bottle_cap = au.elegir("tapa", valid_id, "Etiq", caps, SCALE)

        dirtiness = au.elegir("Suciedad", valid_id, "Etiq", caps, SCALE)
        brand = au.elegir("Marca", valid_id, "Etiq", caps, SCALE)
        reference = au.elegir(brand, valid_id, "Ref", caps, SCALE)
        damage = au.elegir("Dano", valid_id, "Etiq", caps, SCALE)

        Etiqueta = {
            "Material": material,
            "Package color" : package_color,
            "Packaging type": packaging_type,
            "Capacity": capacity,
            "Bottle cap": bottle_cap,
            "Dirtiness": dirtiness,
            "Damage": damage,
            "Brand": brand,
            "Reference": reference,
        }
        
        with open (os.path.join(ruta, "O_" + id + '.json'), 'w') as f:
            json.dump(Etiqueta, f)
        
        print("Ingrese c si desea continuar etiquetando el mismo residuo")
        reuse = input()
        if reuse != "c":
            break

        else:
            mismoResiduo(caps, valid_id, material, package_color, packaging_type, capacity, bottle_cap, dirtiness, brand, reference)

if __name__ == '__main__':
    main()
