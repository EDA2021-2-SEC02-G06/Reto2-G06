"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time 
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Las n obras más antiguas para un medio especifico")
    print("3 - Número total de obras de obras de x Nacionalidad")

catalog = None

#def initCatalog():
 #   return controller.initCatalog()

def loadData(catalog):

    controller,loadData(catalog)

def PrintMediumAniguo(ordenado, num):
   i = 0 
   
   for obra in lt.iterator(ordenado):
        if i < num:
           print(obra)
        i += 1




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        print("Obras cargadas " + str(controller.ObrasSize(catalog)))
        print("Artistas cargados " + str(controller.ArtistasSize(catalog)))

    elif int(inputs[0]) == 2:
        StartTime = time.process_time()
        med = input("Que medio desea vizualizar: ")
        num = int(input("Cuantas obras más antiguas desea ver: "))
        aver = controller.getMediumAntiguo(catalog, med)
        ordenado = controller.ordenar(aver["obras"])
        print("__________________")
        print("Las "+ str(num) + " obras más antiguas son: ")
        PrintMediumAniguo(ordenado, num)
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")
        print(catalog["idartista"])

    elif int(inputs[0]) == 3:
        StartTime = time.process_time()
        pais = input("Que nacionalidad desea analizar: ")
        tabla_nacionalidad = controller.HashNacionalidad(catalog)
        entry3 = mp.get(tabla_nacionalidad, pais)
        numero = me.getValue(entry3)
        print("El número de obras pertenecientes a esta nacionalidad son: " + str(numero))
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")


    else:
        sys.exit(0)
sys.exit(0)
