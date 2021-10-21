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
from DISClib.Algorithms.Sorting import mergesort as ms
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

    catalog["nombre_artista"] = mp.newMap(20000,
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
    addNombreArtista(catalog, artista)

    
   
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

#def NewNacionalidad():
    
 #   meter = {"obras": None, "num": 0}
  #  meter["obras"] = lt.newList("ARRAT_LIST")
   # return meter
    




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
    cmp = cmpFunctionDate
    sorted_list = mr.sort(lista,cmp)
    
    
    return sorted_list












































































































































































































































"""REQUERIMIENTO 3"""

def Encontrar_Artista_ID(nombre, catalog):
    
    for artist in lt.iterator(catalog["artistas"]):
        if nombre in artist["DisplayName"]:
            return artist["ConstituentID"] 
          
            

def Map_Tecnicas_Artista(catalog, nombre):

    cata_artista = catalog["nombre_artista"]
    artista = mp.get(cata_artista, nombre)["value"]
    codigo = artista["ConstituentID"]
    

    Medium_Mejorado = mp.newMap(200,
                            maptype = "PROBING", 
                            loadfactor = 0.8,
                            comparefunction = None)

    cantidad_obras = 0

    for obras in lt.iterator(catalog["obras"]):
        if "," in obras["ConstituentID"]:
            variable = obras["ConstituentID"]
            lista_codigos = variable.split()
            for codigos in lista_codigos:
                if codigo == codigos:
                    if mp.contains(Medium_Mejorado, obras["Medium"]):
                        entrada = mp.get(Medium_Mejorado, obras["Medium"])
                        valor = me.getValue(entrada)
                        dict_ayuda = {"titulo": obras["Title"], "fecha": obras["Date"], "tecnica": obras["Medium"], "dimensiones": obras["Dimensions"]}
                        lt.addLast(valor, dict_ayuda)
                        me.setValue(entrada, valor)
                        cantidad_obras += 1
                    else:
                        dict_ayuda = {"titulo": obras["Title"], "fecha": obras["Date"], "tecnica": obras["Medium"], "dimensiones": obras["Dimensions"]}
                        lista = lt.newList("ARRAY_LIST")
                        lt.addFirst(lista, dict_ayuda)
                        mp.put(Medium_Mejorado, obras["Medium"], lista)
                        cantidad_obras += 1
        else:
           
            id_base = obras["ConstituentID"]
            id_modif = id_base.replace("[", "").replace("]", "")
            if codigo == id_modif:
                    if mp.contains(Medium_Mejorado, obras["Medium"]):
                        entrada = mp.get(Medium_Mejorado, obras["Medium"])
                        valor = me.getValue(entrada)
                        dict_ayuda = {"titulo": obras["Title"], "fecha": obras["Date"], "tecnica": obras["Medium"], "dimensiones": obras["Dimensions"]}
                        lt.addLast(valor, dict_ayuda)
                        me.setValue(entrada, valor)
                        cantidad_obras += 1

                    else:
                        dict_ayuda = {"titulo": obras["Title"], "fecha": obras["Date"], "tecnica": obras["Medium"], "dimensiones": obras["Dimensions"]}
                        lista = lt.newList("ARRAY_LIST")
                        lt.addFirst(lista, dict_ayuda)
                        mp.put(Medium_Mejorado, obras["Medium"], lista)
                        cantidad_obras += 1

    print(nombre + " con el ID en el MoMa número " + str(codigo) + " tiene " + str(cantidad_obras) + " obras a su nombre en el museo.")
    print("Existen " + str(mp.size(Medium_Mejorado)) + " distintas técnicas en su trabajo artistico")

    llaves = mp.keySet(Medium_Mejorado)
    lista_tamaños = lt.newList("ARRAY_LIST")

    for llave in lt.iterator(llaves):
        lista_ob = mp.get(Medium_Mejorado, llave)["value"]
        tamaño = lt.size(lista_ob)
        dict_ayuda2 = {"tecnica": llave, "tamaño": tamaño}
        lt.addLast(lista_tamaños, dict_ayuda2)
    
    r = ms.sort(lista_tamaños, CmpTamaño)

    llave_imprimir = ""
    i = 0
    for dicts in lt.iterator(lista_tamaños):
        if i < 5:
            print(dicts)
            if i == 0:
                llave_imprimir = dicts["tecnica"]
        i += 1
    
    print("La tecnica mas utilizada fue: " + str(llave_imprimir))
    
    valor_imprimir = mp.get(Medium_Mejorado, llave_imprimir)["value"]
    
    
    a = 0
    for obras in lt.iterator(valor_imprimir):
        if a < 3:
            print(obras)
            print("")
            print("-----------------------")
            print("")

    return Medium_Mejorado

def CmpTamaño(obra1, obra2):

    return obra1["tamaño"]>obra2["tamaño"]


    
        

def idaf(nombre, catalog):

    a = None

    for artist in lt.iterator(catalog["artistas"]):
        if nombre in artist["DisplayName"]:
            a = artist

    print(a)
    print(a["ConstituentID"])
    return a["ConstituentID"]   

def addNombreArtista(catalog, artista):

    try:
        nombre_artista = catalog["nombre_artista"]
        if(artista["DisplayName"] != "" and artista["DisplayName"] != None):
            nom_artista = artista["DisplayName"]
            
        else:
            nom_artista = "Unknown"

        mp.put(nombre_artista, nom_artista, artista) 

    except Exception:
        return None
    
def Map_Departamentos(catalog, dpto):

    Departamentos = mp.newMap(200,
                            maptype = "PROBING", 
                            loadfactor = 0.8,
                            comparefunction = None)


    for obras in lt.iterator(catalog["obras"]):

        if mp.contains(Departamentos, obras["Department"]):
            entrada = mp.get(Departamentos, obras["Department"])
            valor = me.getValue(entrada)
            dict_ayuda = {"titulo": obras["Title"], "artistaid": obras["ConstituentID"], "clasificacion": obras["Classification"], "fecha": obras["Date"], "medio": obras["Medium"], "dimensiones": obras["Dimensions"], "peso": obras["Weight (kg)"], "costo": 0, "diametro": obras["Diameter (cm)"], "altura": obras["Height (cm)"], "largo": obras["Length (cm)"], "ancho": obras["Width (cm)"]}
            lt.addLast(valor, dict_ayuda)
            me.setValue(entrada, valor)
        else:
            
            dict_ayuda = {"titulo": obras["Title"], "artistaid": obras["ConstituentID"], "clasificacion": obras["Classification"], "fecha": obras["Date"], "medio": obras["Medium"], "dimensiones": obras["Dimensions"], "peso": obras["Weight (kg)"], "costo": 0, "diametro": obras["Diameter (cm)"], "altura": obras["Height (cm)"], "largo": obras["Length (cm)"], "ancho": obras["Width (cm)"]}
            lista = lt.newList("ARRAY_LIST")
            lt.addFirst(lista, dict_ayuda)
            mp.put(Departamentos, obras["Department"], lista)
    
    obras = mp.get(Departamentos, dpto)["value"]
   
    for obra in lt.iterator(obras):
        
        if obra["diametro"] != "":
            vard = float(obra["diametro"])
            vard1 = (vard/2)/100
            obra["diametro"] = vard1
        
        if obra["altura"] != "":
            vara = float(obra["altura"])
            vara1 = vara/100
            obra["altura"] = vara1
            

        if obra["ancho"] != "":
            varc = float(obra["ancho"])
            varc1 = varc/100
            obra["ancho"] = varc1
        
        if obra["largo"] != "":
            varl = float(obra["largo"])
            varl1 = varl/100
            obra["largo"] = varl1
        
        valor = 0
        valor1 = 0
        if obra["largo"] and obra["ancho"] and obra["altura"] != "":
            tam3 = obra["largo"] * obra["ancho"] * obra["altura"]
            precio3 = 72.00*tam3
            valor = precio3
        
        elif obra["largo"] and obra["ancho"] != "":
            tam2 = obra["largo"] * obra["ancho"]
            precio2 = 72.00*tam2
            valor = precio2
        
        elif obra["ancho"] and obra["altura"] != "":
            tam2 = obra["altura"] * obra["ancho"]
            precio2 = 72.00*tam2
            valor = precio2

        elif obra["largo"] and obra["altura"] != "":
            tam2 = obra["largo"] * obra["altura"]
            precio2 = 72.00*tam2
            valor = precio2
        
        elif obra["altura"] and obra["diametro"] != "":
            tam3r = 3.14 * (obra["diametro"]**2) * obra["altura"]
            precio3r = 72.00*tam3r
            valor = precio3r
        
        elif obra["diametro"] != "":
            tam2r = 3.14 * obra["diametro"]**2
            precio2r = 72.00*tam2r
            valor = precio2r
        
        if obra["peso"] != "":
            preciop = 72.00*float(obra["peso"])
            valor1 = preciop
        
        if valor1 > valor:
            obra["costo"] = valor1
        elif valor > valor1:
            obra["costo"] = valor
        elif valor == valor1:
            obra["costo"] = 48.00

        if obra["fecha"] == "":
            obra["fecha"] = "2021"
    
    d = ms.sort(obras, CmpCosto)
    e = 0
    for obra in lt.iterator(obras):
        if e < 5:
            print(obra)
            print("------------------------------------------------")
        e += 1
    print("")
    print("")
    print("------------------------------------")
    print("------------------------------------")
    print ("")
    print("")
    f = ms.sort(obras, CmpAño)
    h = 0
    for obra in lt.iterator(obras):
        if h < 5:
            print(obra)
            print("-----------------------------------------")
        h += 1
    
    return Departamentos

def CmpCosto(obra1, obra2):

    return obra1["costo"]>obra2["costo"]

def CmpAño(obra1, obra2):

    return obra1["fecha"]<obra2["fecha"]

def Depto_Especifico(dpto, Map_Depto):

    obras = mp.get(Map_Depto, dpto)

    return obras

def funcion_madre(catalog, numero, fecha_ini, fecha_fini):

    Madre = mp.newMap(200,
                            maptype = "PROBING", 
                            loadfactor = 0.8,
                            comparefunction = None)


    for obras in lt.iterator(catalog["obras"]):

        if mp.contains(Madre, obras["Date"]):
            entrada = mp.get(Madre, obras["Date"])
            valor = me.getValue(entrada)
            lt.addLast(valor, obras)
            me.setValue(entrada, valor)
        else:
            
            lista = lt.newList("ARRAY_LIST")
            lt.addFirst(lista, obras)
            mp.put(Madre, obras["Date"], lista)
    
    diferencia  = int(fecha_fini) - int(fecha_ini)
    lista_fechas = lt.newList("ARRAY_LIST")
    i = 0
    while i <= diferencia:
        fecha = int(fecha_ini) + i
        fech = str(fecha)
        lt.addLast(lista_fechas, fech)
        i += 1
    
    Hijo = mp.newMap(100,
                            maptype = "PROBING", 
                            loadfactor = 0.8,
                            comparefunction = None)
    
    for fecha in lt.iterator(lista_fechas):

            if mp.contains(Madre, fecha):
                entrada = mp.get(Madre, fecha)
                valor = me.getValue(entrada)
                
                for elementos in lt.iterator(valor):
                    if "," in elementos["ConstituentID"]:

                        variable = elementos["ConstituentID"].replace("[", "").replace("]", "")
                        lista_codigos = variable.split(",")
                        for codigos in (lista_codigos):
                            codice = codigos.strip()
                            if mp.contains(Hijo, codice):
                                entre = mp.get(Hijo, codice)["value"]
                                lt.addLast(entre, elementos)


                            
                            else: 

                                lista_hijo = lt.newList("ARRAY_LIST")
                                lt.addFirst(lista_hijo, elementos)
                                mp.put(Hijo, codice, lista_hijo)

                    else:
                            id_basee = elementos["ConstituentID"]
                            id_modiff = id_basee.replace("[", "").replace("]", "")
                            
                            if mp.contains(Hijo, id_modiff):
                                entree = mp.get(Hijo, id_modiff)["value"]
                                lt.addLast(entree, elementos)

                            else: 

                                lista_hijo = lt.newList("ARRAY_LIST")
                                lt.addFirst(lista_hijo, elementos)
                                mp.put(Hijo, id_modiff, lista_hijo)

    lista_cod = mp.keySet(Hijo)
    



    
    lista_codigo = lt.newList("ARRAY_LIST")
    for date in lt.iterator(lista_fechas):

        if mp.contains(Madre, date):
            entra = mp.get(Madre, date)["value"]

            for obra in lt.iterator(entra):
                if "," in obra["ConstituentID"]:

                    variable = obra["ConstituentID"].replace("[", "").replace("]", "")
                    lista_codigos = variable.split(",")
                    for codigos in (lista_codigos):
                        codice = codigos.strip()
                        lt.addLast(lista_codigo, codice)
                        

                else:
                        id_base = obra["ConstituentID"]
                        id_modif = id_base.replace("[", "").replace("]", "")
                        lt.addLast(lista_codigo, id_modif)
                        
    lista_dict_codigos = lt.newList("ARRAT_LISt")
    for cod in lt.iterator(lista_codigo):
        dict_ayuda3 = {"codigo": cod, "num": 1}
        Tru = True
        for elementos in lt.iterator(lista_dict_codigos):
            if cod == elementos["codigo"]:
                elementos["num"] = elementos["num"] + 1
                Tru = False
        if Tru == True:
            lt.addFirst(lista_dict_codigos, dict_ayuda3)

    p = ms.sort(lista_dict_codigos, CmpCantidad)

    u = 0
    o = 1
    nomu = []
    for element in lt.iterator(lista_dict_codigos):        
        

        if u < numero:

            arte  = mp.get(catalog["idartista"], element["codigo"])["value"]
            print(arte["ConstituentID"] + " -- " + arte["DisplayName"] + " -- " + arte["BeginDate"] + " -- "+ arte["Gender"] + " -- " + str(element["num"]))    
            print("-----------------------------------------------------------")
        
        if o <= numero:
            nomu.append(arte["DisplayName"])

        u += 1
        o += 1
    
    print("")
    print("")
    print("")

    x = 0
    y = 0
    for elements in lt.iterator(lista_dict_codigos):
        
        ñ = 0
        if y < numero:
            print(nomu[y])
            print("")

        if x < numero:
            print(elements["codigo"])
            imprimir = mp.get(Hijo, elements["codigo"])["value"]
            for im in lt.iterator(imprimir):
            
                if ñ < 5: 
                    print(im["Title"] + " -- " + im["Date"] + " -- " + im["DateAcquired"] + " -- " + im["Medium"] + " -- " + im["Department"] + " -- " + im["Classification"] + " -- " + im["Dimensions"])
                    
                    print ("------------------------------------------------------------------------------------------------------")
                    ñ += 1
        
            print("")
            print("")
            print("")
        x += 1
        y += 1 

    


    return Hijo

def CmpCantidad(obra1, obra2):

    return obra1["num"] > obra2["num"]
