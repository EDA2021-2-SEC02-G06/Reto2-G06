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


from typing import Counter
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
    print("1 - Cargar información en el catálogo")
    print("2 - Las n obras más antiguas para un medio especifico")
    print("3 - Número total de obras de obras de x Nacionalidad")
    print("4 - REQUERIMIENTO 1")
    print("5 - REQUERIMIENTO 2")
    print("6 - REQUERIMIENTO 3 - Obras de un artista clasificado por tecnicas")
    print("7 - REQUERIMIENTO 4")
    print("8 - REQUERIMIENTO 5")
    print("9 - REQUERIMIENTO 6")
    print("10 - FIN DEL PROGRAMA")


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

    elif int(inputs[0]) == 4:
        """ REQUERIMIENTO 1"""
        StartTime = time.process_time()

        fecha_inicio = int((input("Ingrese el año inicial: ")))
        fecha_fin = int(input("Ingrese el año final: "))

        mapa,contador= controller.initArtistCrono(catalog,fecha_inicio,fecha_fin)
        lista_artistas = controller.ordenar(mp.keySet(mapa))
        primeros = controller.req1primeros (mapa,lista_artistas)
        ultimos = controller.req1ultimos(mapa,lista_artistas)

        print("------- PRIMEROS Y ULTIMOS TRES ARTISTA NACIDOS ENTRE "+str(fecha_inicio)+" Y "+str(fecha_fin)+" -------")

        print("| NOMBRE |"+"    "+"| AÑO DE NACIMIENTO |" +"    " + "| AÑO DE FALLECIMIENTO |"+"    "+"| NACIONALIDAD |"+"    "+"| GÉNERO |"+"    ")


        strike = 0
        for artist in lt.iterator(primeros):
            if strike < 3:
                print(artist["DisplayName"]+"   "+artist["BeginDate"]+"   "+artist["EndDate"]+"   "+artist["Nationality"]+"   "+artist["Gender"])
                strike +=1

        print("_____________________")

        
        counter = 0
        for artist in lt.iterator(ultimos):
            if counter < 3:
                print(artist["DisplayName"]+"   "+artist["BeginDate"]+"   "+artist["EndDate"]+"   "+artist["Nationality"]+"   "+artist["Gender"])
                counter +=1
        
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")
        
    
    elif int(inputs[0]) == 5:
        """REQUERIMIENTO 2"""

        fecha_inicio = (input("Ingrese la fecha inicial (AAAA-MM-DD):"))
        fecha_fin = (input("Ingrese la fecha final (AAAA-MM-DD):"))

        mapa,contador= controller.initObrasCrono(catalog,fecha_inicio,fecha_fin)
        lista_artistas = controller.ordenar(mp.keySet(mapa))
        primeros = controller.req1primeros (mapa,lista_artistas)
        ultimos = controller.req1ultimos(mapa,lista_artistas)

        prime_auto,ulti_auto = controller.obtenerArtist(primeros,ultimos,catalog)

        

        

        print("------- PRIMEROS Y ULTIMAS TRES OBRAS ENTRE "+str(fecha_inicio)+" Y "+str(fecha_fin)+" -------")

        print("| TITULO |"+"    "+"| ARTISTA(S) |" +"    " + "| FECHA |"+"    "+"| MEDIO |"+"    "+"| DIMENSIONES |"+"    ")

        strike = 0
        for artist in lt.iterator(prime_auto):
            if strike < 3:
                print(artist["Title"]+"   "+artist["ConstituentID"]+"   "+artist["Date"]+"   "+artist["Medium"]+"   "+artist["Dimensions"])
                strike +=1

        print("_____________________")

        counter = 0
        for artist in lt.iterator(ulti_auto):
            if counter < 3:
                print(artist["Title"]+"   "+artist["ConstituentID"]+"   "+artist["Date"]+"   "+artist["Medium"]+"   "+artist["Dimensions"])
                counter +=1

    



    elif int(inputs[0]) == 6:
        """REQUERIMIENTO 3"""
        nombre = input("¿Cuál es el nombre del artista? ")
        StartTime = time.process_time()
        Map_Tecnicas = controller.Map_Tecnicas_Artista(catalog, nombre)
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")
        
        


    elif int(inputs[0]) == 7:
        """REQUERIMIENTO 4"""


        
        

    elif int(inputs[0]) == 8:
        """REQUERIMIENTO 5"""
        StartTime = time.process_time()
        dpto = input("¿Qué departamento desea analizar? ")
        Map_Depto = controller.Map_Departamentos(catalog, dpto)
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")

    elif int(inputs[0]) == 9:
        """REQUERIMIENTO 6"""
        StartTime = time.process_time()
        numero = int(input("¿Cuantos artistas desea ver? "))
        fecha_ini = input("¿Cuál es el año inicial? ")
        fecha_fini = input("Cuál es el año final? ")
        print("")
        print("")
        funcion_madre = controller.funcion_madre(catalog, numero, fecha_ini, fecha_fini)
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")

    elif int(inputs[0]) == 10:
        """FIN"""

    else:
        sys.exit(0)
sys.exit(0)
