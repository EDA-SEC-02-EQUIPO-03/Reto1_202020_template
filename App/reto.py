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
    print("6- Crear ranking del género")
    print("0- Salir")

def less(element1, element2,condition):
    if float(element1[condition]) < float(element2[condition]):
        return True
    return False

def greater(element1, element2,condition):
    if float(element1[condition]) > float(element2[condition]):
        return True
    return False


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


def ranking_de_peliculas(lst,rank,parameter,orden):
    t1_start = process_time()
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

    #lt.insertionSort(tempo,o,p)
    #lt.selectionSort(tempo,o,p)
    lt.shellsort(tempo,o,p)
    for j in range(1,rank):
        final.append(lt.getElement(tempo,j))
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    print('Top ',rank,' ',d,'',parameter,': \n',final) #impresion final de los datos con la lista, el largo de la lista y los parametros de orden
  
def ranking_de_genero(lst,rank,parameter,orden,genero):
    t1_start = process_time()
    average=0
    count=0
    n=0
    final=[] #list donde se almacena la lista ordenada de nombresP
     #criterio de de puntuacion
    o=less #sentido de la lista
    d='WORST '
    p='vote_average' #prefijo para el print
    if orden.lower() == 'ascendente': #definir orden
        o=greater
        d='BEST'
    if parameter.lower() == 'votos contados': #definir criterio
        p='vote_count'   
    #lt.insertionSort(tempo,o,p)
    #lt.selectionSort(tempo,o,p)
    lt.shellsort(lst,o,p)
    j=0
    while j<rank:
            g=lt.getElement(lst,j)['genres']
            if g==genero:
                average+= float(lt.getElement(lst,j)["vote_average"])
                n+=1
                count+= int(lt.getElement(lst,j)["vote_count"])
                lt.addLast(final,(lt.getElement(lst,j)['original_title']))
            else:
                rank+=1
            j+=1
    if n!=0:
        prom_vave=round(average/n,2)
        prom_vcount=count//n
    else:
        prom_vave=0
        prom_vcount=0
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return [final,prom_vave,prom_vcount,d]
    
    

def entender_un_genero(lst, genres):
    t1_start = process_time()
    final=lt.newList()
    promedio=0
    tamaño=0
    for i in lt.size(lst):
        if lt.getElement(lst, i)["genres"] == genres:
            lt.addLast(final,lt.getElement(lst, i))
            promedio+=lt.getElement(lst,i)["vote_count"]
    tamaño=lt.size(final)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    print("Del genero "+genres+" se obtuvieron "+tamaño+" con votacion promedio de "+round(promedio/tamaño,2)+": \n"+final)
    

def conocer_a_un_director(criteria,lista1,lista2):

    t1_start = process_time()
    lstpeli=[]
    sum_vote=0
    cant_vote=0
    for i in range(1,lt.size(lista1)+1):
                    valor1=lt.getElement(lista1,i)
                    valor2=lt.getElement(lista2,i)
                    n=valor2['director_name']
                    if criteria==n:
                        pelicula=valor1["original_title"]
                        lstpeli.append(pelicula)
                        vote=valor1["vote_average"]
                        sum_vote+=float(vote)
                        cant_vote+=1     
    num_pelis=len(lstpeli)
    prom= sum_vote/cant_vote
    t1_stop = process_time() 
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return [lstpeli,num_pelis,prom]

def loadCast():
    lst = loadCSVFile("themoviesdb/MoviesCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadMovies():
    lst = loadCSVFile("themoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def conocerActor(lst1, lst2, actor):
    titulos=lt.newList('ARRAY_LIST')
    prom=0
    count=0
    mejordirector=''
    directores={}
    for i in range(1,lt.size(lst1)+1):
        pelicula_C=lt.getElement(lst2,i)
        if pelicula_C['actor1_name']==actor or pelicula_C['actor2_name']==actor or pelicula_C['actor3_name']==actor or pelicula_C['actor4_name']==actor or pelicula_C['actor5_name']==actor:
            pelicula=lt.getElement(lst1,i)
            director=pelicula_C['director_name'] 
            titulo=pelicula['title']
            prom+=float(pelicula['vote_average'])
            lt.addLast(titulos,titulo)
            if director in directores:
                directores[director]+=1
                if directores[director]>directores[mejordirector]:
                    mejordirector=director
            elif mejordirector == "":
                directores[director]=1
                mejordirector=director
            else:
                directores[director]=1
            count+=1
    prom=prom/count

    return prom,count,titulos,mejordirector

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
                    ranking_de_peliculas(lstmovies,10,"vote_count","ascendente")
                pass

            elif int(inputs[0])==3: #opcion 3
                if lstmovies==None or lt.size(lstmovies)==0:
                    print("la lista esta vacia")
                if lstcast==None or lt.size(lstcast)==0:
                    print("la lista esta vacia")
                else:
                    criteria=input("Nombre del director que desea conocer")
                    counter=conocer_a_un_director(criteria,lstmovies,lstcast)
                    print("Las peliculas del director ",criteria,"son ",counter[1]," las cuales se nombraran en el siguiente listado:")
                    for k in counter[0]:
                            print(k)
                    print("Las anteriores tienen un promedio de votación de: ",counter[2])
            elif int(inputs[0])==4: #opcion 4
                actor= input('Escriba el nombre del actor que quiere conocer\n')
                info= conocerActor(lstmovies,lstcast,actor)
                print("El actor",actor,"tiene",info[1],"peliculas con un promedio de calificaciones de",info[0]," las cuales son:\b" )
                for i in range(1,lt.size(info[2])+1):
                    print(lt.getElement(info[2],i),"\b")
                print("El director con quien tiene mayor cantidad de colaboraciones es ",info[3])

            elif int(inputs[0])==6: #opcion 6
                if lstmovies==None or lt.size(lstmovies)==0:
                    print("la lista de MOVIES DETAILS  esta vacia")
                else:
                    gen=input("¿De qué género desea hacer el ranking? ")
                    rank=int(input("¿Cuántas peliculas quiere en el ranking? "))
                    if rank <10:
                        print("El numero de peliculas del ranking debe ser mayor o igual a 10" )
                    else:
                        doa=input("¿Desea que sea ascendente o descendente? ")
                        ing=ranking_de_genero(lstmovies,rank,"vote_count",doa,gen)
                        print("El top ",rank," de peliculas",ing[3]," de genero ",gen," es: ")
                        r=1
                        for i in ing[0]:
                                print(r,"->",i)
                                r+=1
                        print("Este ranking tiene un promedio de votos de: ",ing[2]," y la calificación del ranking es: ",ing[1])
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()