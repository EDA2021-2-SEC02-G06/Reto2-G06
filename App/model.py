"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mr
from datetime import datetime as dt
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {"artistas": None,
                "obras": None,
                "medium": None,
                "idartistas": None}

    catalog["artistas"] = lt.newList("ARRAY_LIST", cmpfunction=None)
    catalog["obras"] = lt.newList("ARRAY_LIST", cmpfunction=None)

    catalog["medium"] = mp.newMap(20000,
                                  maptype = "PROBING",
                                  loadfactor = 0.8,
                                  comparefunction=compareMedium)
    
    catalog["idartista"] = mp.newMap(20000,
                                    maptype = "PROBING", 
                                    loadfactor = 0.8,
                                    comparefunction = None)

    return catalog
"""
def newMedium(medium):

    tecnica = {"name": "",
                "obras": None,
                "total": 0}
    
    tecnica["name"] = medium
    tecnica["obras"] = lt.newList("ARRAY_LIST")
"""


# Funciones para agregar informacion al catalogo

def addObra(catalog, obra):
    lt.addLast(catalog["obras"], obra)
    #mp.put(catalog["medium"], obra["Medium"], obra)
    addMedium(catalog, obra)

def addArtista(catalog, artista):
    lt.addLast(catalog["artistas"], artista)
    addIDartista(catalog, artista)

    
   
def addMedium(catalog, obra):
    
    try:
        medium = catalog["medium"]
        if (obra["Medium"] != ""):
            esmedium = obra["Medium"]
            
        else:
            esmedium = "Unkown"
            
        existemedium = mp.contains(medium, esmedium)
        if existemedium:
            entry = mp.get(medium, esmedium)
            medi = me.getValue(entry)
            
            
        else:
            medi = NewMedium(esmedium)
            
            mp.put(medium, esmedium, medi)
            
        lt.addLast(medi["obras"], obra)
        #print(obra)
    except Exception:
        return None

def addIDartista(catalog, artista):
    
    try:
        idartista = catalog["idartista"]
        if (artista["ConstituentID"] != "" and artista["ConstituentID"] != None):
            esidartist = artista["ConstituentID"]
            
        else:
            esidartist = "Unkown"

        mp.put(idartista, esidartist, artista)    
        
        
    except Exception:
        return None

def NewMedium(esmedeium):
    
    medi = {"medium": "", "obras": None}
    medi["medium"] = esmedeium
    medi["obras"] = lt.newList("ARRAT_LIST")
    return medi



# Funciones para creacion de datos

def HashNacionalidad(catalog):

    Nacionalidad = mp.newMap(150,
                            maptype = "PROBING", 
                            loadfactor = 0.8,
                            comparefunction = None)

    codigos = lt.newList("ARRAY_LIST")
    informacion = catalog["idartista"]

    for obras in lt.iterator(catalog["obras"]):
        if "," in obras["ConstituentID"]:
            id_base = obras["ConstituentID"]
            id_modif = id_base.replace("[", "").replace("]", "")
            id_mini_list = id_modif.split(",")
            for element in id_mini_list:
                lt.addLast(codigos, element)
        
        else:
            id_base = obras["ConstituentID"]
            id_modif = id_base.replace("[", "").replace("]", "")
            lt.addLast(codigos, id_modif)
    
    

    for elementos in lt.iterator(codigos):
        entry = mp.get(informacion, elementos)
        if entry != None:
            medi = me.getValue(entry)
            nacionalidad_base = medi["Nationality"]
            

            if (nacionalidad_base != ""):
                nacionalidad_fin = nacionalidad_base
                
            else:
                nacionalidad_fin = "Unkown"
            
            
            

            existe_nacionalidad = mp.contains(Nacionalidad, nacionalidad_fin)
            if existe_nacionalidad:
                entry2 = mp.get(Nacionalidad, nacionalidad_fin)
                medi2 = me.getValue(entry2)
                nueva_medi = medi2 +1
                #print(nueva_medi)
                me.setValue(entry2, nueva_medi)
                
                
            else:
                
                mp.put(Nacionalidad, nacionalidad_fin, 1)
                

        #lt.addLast(medi2["obras"])
    return Nacionalidad

def fechasmap(catalog,inicio,fin):

    fechas = mp.newMap(1000,
                            maptype = "CHAINING", 
                            loadfactor = 4,
                            comparefunction = None)
    

    contador = 0

    for artist in lt.iterator(catalog["artistas"]):
        año = int(artist["BeginDate"])
        if (año>=inicio) and (año <= fin) and (año != None) :
            if mp.contains(fechas,año):
                entry = mp.get(fechas,año)
                value = me.getValue(entry)
                lt.addFirst(value,artist)
                mp.put(fechas,año,value)
                contador +=1
            
            else:
                lista = lt.newList("ARRAY_LIST")
                lt.addFirst(lista,artist)
                mp.put(fechas,año,lista)
                contador +=1

    return fechas,contador

def req2(catalogo,inicio,fin):
    fechas = mp.newMap(1000,
                            maptype = "CHAINING", 
                            loadfactor = 4,
                            comparefunction = None)

    inicio = dt.strptime(inicio,"%Y-%m-%d")
    fin = dt.strptime(fin,"%Y-%m-%d")
    
    contador = 0

    for obra in lt.iterator(catalogo["obras"]):
        año_obra = obra["DateAcquired"]
        if año_obra == "" or año_obra == None or año_obra == "Unknow":
            obra["DateAcquired"] == dt.now()
            print(obra["DateAcquired"])

            
        año = dt.strptime(obra["DateAcquired"],"%Y-%m-%d")
        if (año>=inicio) and (año <= fin) :
            if mp.contains(fechas,año):
                entry = mp.get(fechas,año)
                value = me.getValue(entry)
                lt.addFirst(value,obra)
                mp.put(fechas,año,value)
                contador +=1
            
            else:
                lista = lt.newList("ARRAY_LIST")
                lt.addFirst(lista,obra)
                mp.put(fechas,año,lista)
                contador +=1



    return fechas,contador

def req1primeros(mapa,lista):
    primeros = lt.newList("ARRAY_LIST")
    

    for fecha in lt.iterator(lista):
        if lt.size(primeros) < 3:
            entry = mp.get(mapa,fecha)
            value = me.getValue(entry)
            
            for artist in lt.iterator(value):
                lt.addLast(primeros,artist)
            
    return primeros

def req1ultimos(mapa,lista):
    ultimos = lt.newList("ARRAY_LIST")
    sublista = lt.newList("ARRAY_LIST")
    

    for i in range(0,3):
        valor = lt.lastElement(lista)
        lt.removeLast(lista)
        lt.addLast(sublista,valor)

   

    for fecha in lt.iterator(sublista):
        if lt.size(ultimos) < 3 :
            entry = mp.get(mapa,fecha)
            value = me.getValue(entry)
            
            for artist in lt.iterator(value):
                lt.addLast(ultimos,artist)
        
    return ultimos
# Funciones de consulta

def ObrasSize(catalog):

    return lt.size(catalog["obras"])

def ArtistasSize(catalog):

    return lt.size(catalog["artistas"])

def getMediumAntiguo(catalog, med):
    
    medi = mp.get(catalog["medium"], med)
    
    if medi:
        return me.getValue(medi)
    return None


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtistByBeginDate(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'Date' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artist1 < artist2

# Funciones de ordenamiento
def compareMedium(mediumm, med ):
    medentry = me.getKey(med)
    if (mediumm == medentry):
        return 0
    elif (mediumm > medentry):
        return 1
    else:
        return -1
def cmpFunctionDate(obra_uno,obra_dos):

    if obra_uno["Date"] == "" and obra_dos["Date"] == "":
        obra1 = 0
        obra2 = 0
    elif obra_uno["Date"] != "" and obra_dos["Date"] != "":
        obra1 =int(obra_uno["Date"])
        obra2 = int(obra_dos["Date"])

    elif obra_uno["Date"] == "":
        obra1 = 15000
        obra2 = int(obra_dos["Date"])
    
    elif obra_dos["Date"] == "":
        obra1 = int(obra_uno["Date"])
        obra2 = 15000

    return obra1 < obra2


def MergeSort(lista):
    cmp = cmpArtistByBeginDate
    sorted_list = mr.sort(lista,cmp)
    
    
    return sorted_list












































































































































































































































"""REQUERIMIENTO 3"""

def Encontrar_Artista_ID(nombre, catalog):

    for artist in lt.iterator(catalog["artist"]):
        if nombre in artist["DisplayName"]:
            return artist
            break

def Map_Tecnicas_Artista(Id_Artista, catalog):

    #for obra in lt.iterator(catalog["obras"]):
    pass

