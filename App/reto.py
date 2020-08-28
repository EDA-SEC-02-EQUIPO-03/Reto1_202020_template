"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1



def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def ranking_de peliculas(lst,rank,parameter,orden):
    t1_start = process_time():
    tempo=lt.newList() #list donde se almacena la lista desordenada con puntuaciones y nombres
    final=[] #list donde se almacena la lista ordenada de nombresP
    p='vote_average' #criterio de de puntuacion
    o=less #sentido de la lista
    d='WORST ' #prefijo para el print
    if orden.lower() == 'ascendente': #definir orden
        o=greater
        d='BEST'
    if parameter.lower() == 'count': #definir criterio
        p='vote_count'
    tempo=lst.copy()

    #ins.insertionSort(tempo,o,p)
    #sel.selectionSort(tempo,o,p)
    she.shellSort(tempo,o,p)
    for j in range(1,rank):
        final.append(lt.getElement(tempo,j))
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    print('Top ',rank,' ',d,'',parameter,': \n',final) #impresion final de los datos con la lista, el largo de la lista y los parametros de orden
  

def entender_un_genero(lst, genres):
    t1_start = process_time():
    final=lt.newList()
    promedio=0
    tamaño=0
    for i in lt.size(lst):
        if lt.getElement(lst, i)["genre"] == genres:
            lt.addLast(final,lt.getElement(lst, i))
            promedio+=lt.getElement(lst,i)["vote_count"]
    tamaño=lt.size(final)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    print("Del genero "+genres+" se obtuvieron "+tamaño+" con votacion promedio de "+round(promedio/tamaño,2)+": \n"+final)
    

def loadCast():
    lst = loadCSVFile("theMoviesdb/MoviesCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                'Cargando datos'
                lstmovies = loadMovies()
                lstcast = loadCast()

            elif int(inputs[0])==2: #opcion 2
                if lstmovies==None or lstmovies['size']==0:
                    print("la lista esta vacia")
                else:
                    Ranking_de_peliculas(lstmovies,10,"vote_count","ascendente")
                pass

            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==3: #opcion 5
                if lstmovies==None or lstmovies['size']==0:
                    print("la lista esta vacia")
                else:
                    Entender_un_genero(lstmovies,"Drama")
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()