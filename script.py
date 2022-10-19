from datetime import datetime
from xml.dom.expatbuilder import ElementInfo
import PySimpleGUI as sg
from os import mkdir
import keyboard
import sys
import cv2
import os
import json

eCarpeta = os.path.isdir('Observaciones')
nombre_carpeta = "Observaciones"

if eCarpeta == False:
    mkdir(nombre_carpeta)

ruta = os.path.abspath(nombre_carpeta)

print("Cargando camaras y diccionarios...")
with open (os.path.join(ruta, "InfoEtiqueta.json"), 'r') as f:
    diccionarioEtiq = json.load(f)
with open (os.path.join(ruta, "InfoReferencias.json"), 'r') as f:
    diccionarioRef = json.load(f)

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

valid_id = ['0', '1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def enumerarOpcionesReferencias(marca):
    for i, name in enumerate(diccionarioRef[marca].values()):
        _id = valid_id[i]
        print(f'{_id} - {name}')

def enumerarOpcionesEtiqueta(elemento):
    for i, name in enumerate(diccionarioEtiq[elemento].values()):
        _id = valid_id[i]
        print(f'{_id} - {name}')

def elegirMaterial():
    print()
    print("Seleccione el material del residuo a traves del caracter marcado al costado")
    elemento = "Material"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)

        for k in valid_id:
            if key == ord(k):
                material = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return material

def elegirColor():
    print()
    print("Seleccione el color del empaque del residuo a traves del numero marcado al costado")
    elemento = "Color"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)

        for k in valid_id:
            if key == ord(k):
                color = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return color

def elegirTipoempaque():
    print()
    print("Seleccione el tipo de empaque de su resiudo a traves del numero marcado al costado")
    elemento = "tipoEmpaque"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)

        for k in valid_id:
            if key == ord(k):
                tipoEmpaque = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return tipoEmpaque

def elegirCapacidad():
    print()
    print("Seleccione la capacidad del empaque a traves del numero marcado al costado")
    elemento = "Capacidad"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)

        for k in valid_id:
            if key == ord(k):
                capacidad = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return capacidad

def elegirTapa():
    print()
    print("Indique si el residuo viene con tapa")
    elemento = "tapaBotella"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)

        for k in valid_id:
            if key == ord(k):
                tapa = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return tapa

def elegirSuciedad():
    print()
    print("Indique el nivel de suciedad del residuo a traves del numero marcado al costado")
    elemento = "Suciedad"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)

        for k in valid_id:
            if key == ord(k):
                suciedad = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return suciedad

def elegirDano():
    print()
    print("Indique el nivel de daño del residuo a traves del numero marcado al costado")
    elemento = "Dano"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)

        for k in valid_id:
            if key == ord(k):
                nivelDano = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return nivelDano


def elegirMarca():
    print()
    print("Indique la marca del reisuo a traves del numero marcado al costado")
    elemento = "Marca"
    enumerarOpcionesEtiqueta(elemento)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)
        for k in valid_id:
            if key == ord(k):
                marca = diccionarioEtiq[elemento][k]
                cv2.destroyAllWindows()
                return marca

def elegirReferencia(marca):
    print()
    print("Indique la referencia a traves del numero marcado al costado")
    enumerarOpcionesReferencias(marca)

    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        # if frame is read correctly ret is True
        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Imagen1', frame)
        cv2.imshow('Imagen2', frame2)    
        key = cv2.waitKey(1)
        for k in valid_id:
            if key == ord(k):
                referencia = diccionarioRef[marca][k]
                cv2.destroyAllWindows()
                return referencia

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera 1")
    exit()

if not cap2.isOpened():
    print("Cannot open camera 2")
    exit()


if not cap.isOpened():
    print("No se puede abrir la camara 1")
    exit()

if not cap2.isOpened():
    print("No se puede abrir la camara 2")
    exit()

print("Presione x para tomar fotos o e para salir")
while True:
    now = datetime.now()
    dia = format(now.day)
    mes = format(now.month)
    anio = format(now.year)
    hora = format(now.hour)
    minuto = format(now.minute)
    segundo = format(now.second)

    if keyboard.is_pressed("e"):
        break
    
    if keyboard.is_pressed("x"):
        print("Tomando fotos")
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
        
        foto1 = "O_" + str(id) + "-1"
        foto2 = "O_" + str(id) + "-2"        
        strjson = "O_" + str(id)
        
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()

        if not ret or not ret2:
            print("Can't receive frame (stream end?). Exiting ...")

        cv2.imwrite(os.path.join(ruta, foto1 + ".png") , frame)
        cv2.imwrite(os.path.join(ruta, foto2 + ".png") , frame2)
        print("Fotos tomadas correctamente")

        while True:
            print("Iniciando proceso de etiquetado, ingrese e para salir o presione enter para continuar")
    
            a = input()
            if a == "e":
                exit()

            material = elegirMaterial()

            if material == "PET" or material == "PE-HD" or material == "PVC" or material == "PE-LD" or material == "PP" or material == "PS" or material == "Other plastic" or material == "Glass":
                package_color = elegirColor()
              
            packaging_type = elegirTipoempaque()

            if packaging_type == "Bottle" or packaging_type == "Can" or packaging_type == "Box" or packaging_type == "Other":
                capacity = elegirCapacidad()

            if packaging_type == "Bottle" or packaging_type == "Cup":
                bottle_cap = elegirTapa()

            dirtiness = elegirSuciedad()
            damage = elegirDano()
            brand = elegirMarca()
            reference = elegirReferencia(brand)

            

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
            print("Presione x para tomar fotos o e para salir")
            break