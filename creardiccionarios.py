import json
import os 
from os import mkdir

eCarpeta = os.path.isdir('Observaciones')

nombre_carpeta = "Observaciones"
if eCarpeta == False:
    mkdir(nombre_carpeta)

ruta = os.path.abspath(nombre_carpeta)

Etiq = {
    "Material" : {"0":"PET", "1":"PE-HD", "2":"PVC", "3":"PE-LD", "4":"PP", "5":"PS", "6":"Other plastic", "7":"Glass", "8":"Aluminium", "9":"Other metal", "9":"Cardboard", "a":"Paper print", "b":"Newspaper", "c":"Magazine", "d":"Tetrapack", "e":"Other"},
    "Color" : {"0":"Clear transparent", "1":"White transparent", "2":"Red transparent", "3":"Green transparent", "4":"Brown transparent", "5":"Blue transparent", "6":"Colored transparent", "7":"White opaque", "8":"Blue opaque", "9":"Green opaque", "a":"Brown opaque", "b":"Black opaque", "c":"Colored opaque", "d":"Yellow", "e":"Orange", "f":"Purple", "g":"Gray", "h":"Other color"},
    "tipo de empaque": {"0":"Bottle", "1":"Can", "2":"Bag", "3":"Box", "4":"Cup", "5":"Wrapping", "6":"Lid", "7":"Sheet", "8":"Other"},
    "Capacidad": {"0":"0-299", "1":"300-499", "2": "500-999","3": "1000-1499","4": "1500-3000","5": ">3000"},
    "tapa": {"0": True, "1": False},
    "Suciedad": {"0":"Clean", "1": "Small", "2": "Medium", "3":"High"},
    "Dano": {"0":"Mixed", "1":"Damaged", "2":"Undamaged"},
    "Marca": {"0":"Coca-Cola", "1":"Bavaria", "2":"Postobon", "3":"Colanta", "4":"Alpina", "5":"Pepsi", "6":"Nacional de chocolates", "7":"Santin Noel", "8":"Detodito", "9":"Doritos", "a":"Gatorade", "b":"Cheesetris", "c":"Manimoto", "d":"Margarita", "e":"Tosh", "f": "Other"},
}



referencias = {
    "Coca-Cola": {"0": "Zero", "1": "Original", "2": "Other"},
    "Bavaria": {"0": "Pony Malta", "1": "Other"},
    "Postobon": {"0": "Manzana", "1": "Other"},
    "Colanta": {"0": "Yogurt", "1": "Other"},
    "Alpina": {"0": "Bonyurt", "1": "Other"},
    "Pepsi": {"0": "Other"},
    "Nacional de chocolates": {"0": "Chocolatina Jet", "1": "Other"},
    "Santin Noel": {"0": "Original", "1": "Other"},
    "Detodito": {"0": "Other"},
    "Doritos": {"0": "Other"},
    "Gatorade": {"0": "Other"},
    "Cheesetris": {"0": "Other"},
    "Manimoto": {"0": "Other"},
    "Margarita": {"0": "Other"},
    "Tosh": {"0": "Other"},
    "Other":{"0": "Other"}
}

with open (os.path.join(ruta, "InfoEtiqueta.json"), "w") as dicEtiq:
    json.dump(Etiq, dicEtiq)

with open (os.path.join(ruta, "InfoReferencias.json"), "w") as dicRef:
    json.dump(referencias, dicRef)

with open (os.path.join(ruta, "InfoEtiqueta.json"), 'r') as f:
    diccionarioEtiq = json.load(f)

with open (os.path.join(ruta, "InfoReferencias.json"), 'r') as f:
    diccionarioRef = json.load(f)