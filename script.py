from datetime import datetime
import PySimpleGUI as sg
from os import mkdir
import keyboard
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

def elegirMaterial():
    print()
    print("Seleccione el material del residuo a traves del caracter marcado al costado")
    print("0 - PET")
    print("1 - PE-HD")
    print("2 - PVC")
    print("3 - PE-LD")
    print("4 - PP")
    print("5 - PS")
    print("6 - Otro plastico") #Other plastic
    print("7 - Vidrio") #Glass
    print("8 - Aluminio") #Aluminium
    print("9 - Otro metal") #Other metal
    print("a - Carton") #Carton
    print("b - Papel de impresion") #Paper print
    print("c - Periodico") #Newspaper
    print("d - Revista") #Magazine
    print("e - Tetrapack")
    print("f - Otro")
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
    
        if key == ord('0'):
            material = diccionarioEtiq["Material"]["0"]
            break
        elif key == ord('1'):
            material = diccionarioEtiq["Material"]["1"]
            break
        elif key == ord('2'):
            material = diccionarioEtiq["Material"]["2"]
            break
        elif key == ord('3'):
            material = diccionarioEtiq["Material"]["3"]
            break
        elif key == ord('4'):
            material = diccionarioEtiq["Material"]["4"]
            break
        elif key == ord('5'):
            material = diccionarioEtiq["Material"]["5"]
            break
        elif key == ord('6'):
            material = diccionarioEtiq["Material"]["6"]
            break
        elif key == ord('7'):
            material = diccionarioEtiq["Material"]["7"]
            break
        elif key == ord('8'):
            material = diccionarioEtiq["Material"]["8"]
            break
        elif key == ord('9'):
            material = diccionarioEtiq["Material"]["9"]
            break
        elif key == ord('a'):
            material = diccionarioEtiq["Material"]["a"]
            break
        elif key == ord('b'):
            material = diccionarioEtiq["Material"]["b"]
            break
        elif key == ord('c'):
            material = diccionarioEtiq["Material"]["c"]
            break
        elif key == ord('d'):
            material = diccionarioEtiq["Material"]["d"]
            break
        elif key == ord('e'):
            material = diccionarioEtiq["Material"]["e"]
            break

    cv2.destroyAllWindows()
    return material

def elegirColor():
    print()
    print("Seleccione el color del empaque del residuo a traves del numero marcado al costado")
    print("0 - Transparente claro") # Clear transparent
    print("1 - Blanco tranparente") # White transparent
    print("2 - Rojo transparente") # Red transparent
    print("3 - Verde transparente") # Green transparent
    print("4 - Cafe transparente") # Brown transparent
    print("5 - Azul transparente") # Blue transparent
    print("6 - Transparente colorido") # Colored transparent
    print("7 - Blanco opaco") # White opaque
    print("8 - Azul opaco") # Blue opaque
    print("9 - Verde opaco") # Green opaque
    print("a - Cafe opaco") # Brown opaque
    print("b - Negro opaco") # Black opaque
    print("c - Opaco colorido") # Colored opaque
    print("d - Amarillo") # Yellow
    print("e - Naranjado") # Orange
    print("f - Morado") # Purple
    print("g - Gris") # Gray
    print("h - Otro color") # Other color

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
        if key == ord('0'):
            color = diccionarioEtiq["Color"]["0"]
            break
        elif key == ord('1'):
            color = diccionarioEtiq["Color"]["1"]
            break
        elif key == ord('2'):
            color = diccionarioEtiq["Color"]["2"]
            break
        elif key == ord('3'):
            color = diccionarioEtiq["Color"]["3"]
            break
        elif key == ord('4'):
            color = diccionarioEtiq["Color"]["4"]
            break
        elif key == ord('5'):
            color = diccionarioEtiq["Color"]["5"]
            break
        elif key == ord('6'):
            color = diccionarioEtiq["Color"]["6"]
            break
        elif key == ord('7'):
            color = diccionarioEtiq["Color"]["7"]
            break
        elif key == ord('8'):
            color = diccionarioEtiq["Color"]["8"]
            break
        elif key == ord('9'):
            color = diccionarioEtiq["Color"]["9"]
            break
        elif key == ord('a'):
            color = diccionarioEtiq["Color"]["a"]
            break
        elif key == ord('b'):
            color = diccionarioEtiq["Color"]["b"]
            break
        elif key == ord('c'):
            color = diccionarioEtiq["Color"]["c"]
            break
        elif key == ord('d'):
            color = diccionarioEtiq["Color"]["d"]
            break
        elif key == ord('e'):
            color = diccionarioEtiq["Color"]["e"]
            break
        elif key == ord('f'):
            color = diccionarioEtiq["Color"]["f"]
            break
        elif key == ord('g'):
            color = diccionarioEtiq["Color"]["g"]
            break
        elif key == ord('h'):
            color = diccionarioEtiq["Color"]["h"]
            break
    cv2.destroyAllWindows()
    return color

def elegirTipoempaque():
    print()
    print("Seleccione el tipo de empaque de su resiudo a traves del numero marcado al costado")
    print("0 - Botella") # Bottle
    print("1 - Lata") # Can
    print("2 - Bolsa") # Bag
    print("3 - Caja") # Box
    print("4 - Frasco") # Cup
    print("5 - Envoltorio") # Wrapping
    print("6 - Tapa") # Lid
    print("7 - Hoja") # Sheet
    print("8 - Otro") # Other

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
        if key == ord('0'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["0"]
            break
        elif key == ord('1'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["1"]
            break
        elif key == ord('2'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["2"]
            break
        elif key == ord('3'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["3"]
            break
        elif key == ord('4'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["4"]
            break
        elif key == ord('5'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["5"]
            break
        elif key == ord('6'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["6"]
            break
        elif key == ord('7'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["7"]
            break
        elif key == ord('8'):
            tipoEmpaque = diccionarioEtiq["tipoEmpaque"]["8"]
            break
    cv2.destroyAllWindows()
    return tipoEmpaque




def elegirCapacidad():
    print()
    print("Seleccione la capacidad del empaque a traves del numero marcado al costado")
    print("0 - 0-299") # 0-299
    print("1 - 300-499") # 300-499
    print("2 - 500-999") # 500-999
    print("3 - 1000-1499") # 1000-1499
    print("4 - 1500-3000") # 1500-3000
    print("5 - >3000") # >3000
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
        if key == ord('0'):
            capacidad = diccionarioEtiq["Capacidad"]["0"]
            break
        elif key == ord('1'):
            capacidad = diccionarioEtiq["Capacidad"]["1"]
            break
        elif key == ord('2'):
            capacidad = diccionarioEtiq["Capacidad"]["2"]
            break
        elif key == ord('3'):
            capacidad = diccionarioEtiq["Capacidad"]["3"]
            break
        elif key == ord('4'):
            capacidad = diccionarioEtiq["Capacidad"]["4"]
            break
        elif key == ord('5'):
            capacidad = diccionarioEtiq["Capacidad"]["5"]
            break
    cv2.destroyAllWindows()
    return capacidad

def elegirTapa():
    print()
    print("Indique si el residuo viene con tapa")
    print("0 - Si tiene") # TRUE
    print("1 - No tiene") # FALSE
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
        if key == ord('0'):
            tapa = diccionarioEtiq["tapaBotella"]["0"]
            break
        elif key == ord('1'):
            tapa = diccionarioEtiq["tapaBotella"]["1"]
            break
    cv2.destroyAllWindows()
    return tapa


def elegirSuciedad():
    print()
    print("Indique el nivel de suciedad del residuo a traves del numero marcado al costado")
    print("0 - Limpio") # Clean
    print("1 - Poca suciedad") # Small
    print("2 - suciedad media") # Medium
    print("3 - Mucha suciedad") # High
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
        if key == ord('0'):
            suciedad = diccionarioEtiq["Suciedad"]["0"]
            break
        elif key == ord('1'):
            suciedad = diccionarioEtiq["Suciedad"]["1"]
            break
        elif key == ord('2'):
            suciedad = diccionarioEtiq["Suciedad"]["2"]
            break
        elif key == ord('3'):
            suciedad = diccionarioEtiq["Suciedad"]["3"]
            break
    cv2.destroyAllWindows()
    return suciedad

def elegirDano():
    print()
    print("Indique el nivel de daño del residuo a traves del numero marcado al costado")
    print("0 - Semi dañado") # Mixed
    print("1 - Dañado") # Damaged
    print("2 - no dañado") # Undamaged
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
        if key == ord('0'):
            nivelDano = diccionarioEtiq["Dano"]["0"]
            break
        elif key == ord('1'):
            nivelDano = diccionarioEtiq["Dano"]["1"]
            break
        elif key == ord('2'):
            nivelDano = diccionarioEtiq["Dano"]["2"]
            break
    cv2.destroyAllWindows()
    return nivelDano

def elegirMarca():
    print()
    print("Indique la marca del reisuo a traves del numero marcado al costado")
    print("0 - Coca-cola")
    print("1 - Bavaria")
    print("2 - Postobon")
    print("3 - Colanta")
    print("4 - Alpina")
    print("5 - Pepsi")
    print("6 - Nacional de chocolates")
    print("7 - Detodito")
    print("8 - Doritos")
    print("9 - Gatorade")
    print("a - Cheesetris")
    print("b - Manimoto")
    print("c - Margarita")
    print("d - Tosh")
    print("e - Other")
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
        if key == ord('0'):
            marca = diccionarioEtiq["Marca"]["0"]
            break
        elif key == ord('1'):
            marca = diccionarioEtiq["Marca"]["1"]
            break
        elif key == ord('2'):
            marca = diccionarioEtiq["Marca"]["2"]
            break
        elif key == ord('3'):
            marca = diccionarioEtiq["Marca"]["3"]
            break
        elif key == ord('4'):
            marca = diccionarioEtiq["Marca"]["4"]
            break
        elif key == ord('5'):
            marca = diccionarioEtiq["Marca"]["5"]
            break
        elif key == ord('6'):
            marca = diccionarioEtiq["Marca"]["6"]
            break
        elif key == ord('7'):
            marca = diccionarioEtiq["Marca"]["7"]
            break
        elif key == ord('8'):
            marca = diccionarioEtiq["Marca"]["8"]
            break
        elif key == ord('9'):
            marca = diccionarioEtiq["Marca"]["9"]
            break
        elif key == ord('a'):
            marca = diccionarioEtiq["Marca"]["a"]
            break
        elif key == ord('b'):
            marca = diccionarioEtiq["Marca"]["b"]
            break
        elif key == ord('c'):
            marca = diccionarioEtiq["Marca"]["c"]
            break
        elif key == ord('d'):
            marca = diccionarioEtiq["Marca"]["d"]
            break
        elif key == ord('e'):
            marca = diccionarioEtiq["Marca"]["e"]
            break
    cv2.destroyAllWindows()
    return marca

def elegirReferencia(marca):
    if marca == "Coca-Cola":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Zero")
        print("1 - Original")
        print("2 - Otro")
    elif marca == "Bavaria":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Pony Malta")
        print("1 - Otro")
    elif marca == "Postobon":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Manzana")
        print("1 - Otro")
    elif marca == "Colanta":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Yogurt")
        print("1 - Otro")
    elif marca == "Alpina":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Bonyurt")
        print("1 - Otro")
    elif marca == "Pepsi":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Nacional de chocolates":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Chocolatina Jet")
        print("1 - Otro")
    elif marca == "Detodito":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Doritos":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Gatorade":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Cheesetris":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Manimoto":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Margarita":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Tosh":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")
    elif marca == "Other":
        print()
        print("Indique la referencia a traves del numero marcado al costado")
        print("0 - Otro")


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
        if marca == "Coca-Cola":
            if key == ord('0'):
                referencia = diccionarioRef[marca]["0"]
                break
            elif key == ord('1'):
                referencia = diccionarioRef["Coca-Cola"]["1"]
                break
            elif key == ord('2'):
                referencia = diccionarioRef["Coca-Cola"]["2"]
                break
        elif marca == "Bavaria":
            if key == ord('0'):
                referencia = diccionarioRef["Bavaria"]["0"]
                break
            elif key == ord('1'):
                referencia = diccionarioRef["Bavaria"]["1"]
                break
        elif marca == "Postobon":
            if key == ord('0'):
                referencia = diccionarioRef["Postobon"]["0"]
                break
            elif key == ord('1'):
                referencia = diccionarioRef["Postobon"]["1"]
                break
        elif marca == "Colanta":
            if key == ord('0'):
                referencia = diccionarioRef["Colanta"]["0"]
                break
            elif key == ord('1'):
                referencia = diccionarioRef["Colanta"]["1"]
                break
        elif marca == "Alpina":
            if key == ord('0'):
                referencia = diccionarioRef["Alpina"]["0"]
                break
            elif key == ord('1'):
                referencia = diccionarioRef["Alpina"]["1"]
                break
        elif marca == "Pepsi":
            if key == ord('0'):
                referencia = diccionarioRef["Pepsi"]["0"]
                break
        elif marca == "Nacional de chocolates":
            if key == ord('0'):
                referencia = diccionarioRef["Nacional de chocolates"]["0"]
                break
            elif key == ord('0'):
                referencia = diccionarioRef["Nacional de chocolates"]["1"]
                break
        elif marca == "Detodito":
            if key == ord('0'):
                referencia = diccionarioRef["Detodito"]["0"]
                break
        elif marca == "Doritos":
            if key == ord('0'):
                referencia = diccionarioRef["Doritos"]["0"]
                break
        elif marca == "Gatorade":
            if key == ord('0'):
                referencia = diccionarioRef["Gatorade"]["0"]
                break
        elif marca == "Cheesetris":
            if key == ord('0'):
                referencia = diccionarioRef["Cheesetris"]["0"]
                break
        elif marca == "Manimoto":
            if key == ord('0'):
                referencia = diccionarioRef["Manimoto"]["0"]
                break
        elif marca == "Margarita":
            if key == ord('0'):
                referencia = diccionarioRef["Margarita"]["0"]
                break
        elif marca == "Tosh":
            if key == ord('0'):
                referencia = diccionarioRef["Tosh"]["0"]
                break
        elif marca == "Other":
            if key == ord('0'):
                referencia = diccionarioRef["Other"]["0"]
                break

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
                break

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