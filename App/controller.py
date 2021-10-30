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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():

    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    
    loadObras(catalog)
    loadArtistas(catalog)

def loadObras(catalog):

    obrasfile = cf.data_dir + "MoMa/Artworks-utf8-large.csv"
    input_file = csv.DictReader(open(obrasfile, encoding = "utf-8"))
    for obra in input_file:
        model.addObra(catalog, obra)

def loadArtistas(catalog):

    artistasfile = cf.data_dir + "MoMa/Artists-utf8-large.csv"
    input_file = csv.DictReader(open(artistasfile, encoding = "utf-8"))
    for artista in input_file:
        model.addArtista(catalog, artista)

def initArtistCrono(catalog,inicio,fin):
    """
    Llama la función que crea una lista vacía para el requerimiento 1.
    """
    retorno = model.fechasmap(catalog,inicio,fin)
    return retorno

def initObrasCrono(catalog,inicio,fin):
    """
    Llama la función que crea una lista vacía para el requerimiento 1.
    """
    retorno = model.req2(catalog,inicio,fin)
    return retorno
def obtenerArtist(primeros,ultimos,catalogo):

    return model.obtenerArtist(primeros,ultimos,catalogo)

# Funciones de ordenamiento

def ordenar(lista):
    return model.MergeSort(lista)

# Funciones de consulta sobre el catálogo

def ObrasSize(catalog):

    return model.ObrasSize(catalog)

def ArtistasSize(catalog):

    return model.ArtistasSize(catalog)

def getMediumAntiguo(catalog, med):

    return model.getMediumAntiguo(catalog, med)

def HashNacionalidad(catalog):

    return model.HashNacionalidad(catalog)
def req1primeros(mapa,lista):

    return model.req1primeros(mapa,lista)

def req1ultimos(mapa,lista):
    return model.req1ultimos(mapa,lista)



"""REQUERIMIENTO 3"""

def Encontrar_Artista_ID(nombre, catalog):

    model.Encontrar_Artista_ID(nombre, catalog)

def Map_Tecnicas_Artista(catalog, nombre):

    return model.Map_Tecnicas_Artista(catalog, nombre)

def idaf(nombre, catalog):

    model.idaf(nombre, catalog)

def Map_Departamentos(catalog, dpto):

    return model.Map_Departamentos(catalog, dpto)

def Depto_Especifico(dpto, Map_Depto):

    model.Depto_Especifico(dpto, Map_Depto)

def funcion_madre(catalog, numero, fecha_ini, fecha_fini):

    return model.funcion_madre(catalog, numero, fecha_ini, fecha_fini)
