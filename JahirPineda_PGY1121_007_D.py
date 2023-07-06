import os
import msvcrt
import time
import numpy
lista_ruts = []
lista_filas = (1,2,3,4,5,6,7,8,9,10)
lista_columnas = ('A','B','C','D','E','F','G','H','I','J')
lista_ubicaciones = []
acumulador_entradas = ()
acumulador_premium = ()
acumulador_gold = ()
acumulador_silver = ()
def ver_menu():
    print("""Menu Creativos.cl
    1.       Comprar entradas
    2.       Mostrar ubicaciones disponibles
    3.       Ver listado de asistentes
    4.       Mostrar ganancias totales
    5.       SALIR
    """)

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR!, ingrese una opcion entre 1 y 5")
        except:
            print("ERROR, debe ingresar un numero entero!")

time.sleep(3)       
def comprar_entradas():
    while True:
        try:
            cantidad_entradas = int(input("Ingrese cantidaD de entradas deseadas(maximo 3!!): "))
            if cantidad_entradas >= 1 and cantidad_entradas <= 3:
                return cantidad_entradas
            else:
                print("Ingrese una cantidad entre 1 y 3")
        except:
            print("ERROR, ingrese un numero entero!!")      

def validar_tipo_entrada():
    ver_ubicaciones() 
    while True:
        try:
            entrada = int(input("""Ingrese entrada que desea comprar:
            1. PLATINUM($120.000 Asientos del 1 al 20)
            2. GOLD($80.000 Asientos del 21 al 50)
            3. SILVER($50.000 Asientos del 51 al 100"""))
            if entrada in(1,2,3):
                return entrada
            else:
                print("Por favor ingrese una opcion entre 1 y 3")
        except:
            print("ERROR, ingrese un número entero")    
        
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut de persona para quien es la entrada(sin puntos ni codigo verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                print("Rut registrado a entrada!")
                return rut
            else:
                print("Ingrese un rut entre 1000000 y 99999999")
        except:
            print("ERROR, debe ingresar un numero entero")


def ver_ubicaciones():
    print("      A  B  C  D  E  F  G  H  I  J")
    for x in range(10):
        print(f"fila",lista_filas{x},end="\t")
        for y in range(10):
            return ver_menu
       


def ver_asistentes():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut in lista_ruts:
                print
            else:
                print("Rut no registrado")
        except:
            print("ERROR, ingrese un numero entero!")


def mostrar_ganancias():
    while True:
       print({acumulador_gold}+{acumulador_premium}+{acumulador_silver})


def mensaje_despedida():
    print("Jahir Pineda, 06-07-2023")
