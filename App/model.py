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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {"artistas": None,
                "obras": None,
                "medium": None}

    catalog["artistas"] = lt.newList("ARRAY_LIST", cmpfunction=None)
    catalog["obras"] = lt.newList("ARRAY_LIST", cmpfunction=None)

    catalog["medium"] = mp.newMap(20000,
                                  maptype = "CHAINING",
                                  loadfactor = 7.0,
                                  comparefunction=None)

    return catalog

def newMedium(medium):

    tecnica = {"name": "",
                "obras": None,
                "total": 0}
    
    tecnica["name"] = medium
    tecnica["obras"] = lt.newList("ARRAY_LIST")
# Funciones para agregar informacion al catalogo

def addObra(catalog, obra):
    lt.addLast(catalog["obras"], obra)
    mp.put(catalog["medium"], obra["Medium"], obra)
    

def addArtista(catalog, artista):
    lt.addLast(catalog["artistas"], artista)
    
"""    
def addMedium(catalog, obra):
    
    try: 
        medium = catalog["medium"]
        if (obra["medium"] != ""):
            esmedium = obra["medium"]
        else:
            esmedium = "Unkown"
"""
#def addMedium(catalog, obra):
 #   mp.put(catalog["medium"], obra["Medium"], obra)
# Funciones para creacion de datos

# Funciones de consulta

def ObrasSize(catalog):

    return lt.size(catalog["obras"])

def ArtistasSize(catalog):

    return lt.size(catalog["artistas"])

def getMediumAntiguo(catalog, med):
    
    medi = mp.get(catalog["medium"], med)
    print(medi)
    if medi:
        print(me.getValue(medi)["obras"])
    print("Fallo")

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
