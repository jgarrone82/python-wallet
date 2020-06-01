"""
    @author: Jorge Garrone
    Opcion5.py:
        Funciones para la opción 5 del sistema de Criptomonedas
"""
from Funciones import es_moneda, get_precio, actualizar_dato, es_numero
from Funciones import es_mi_codigo, obtener_cantidad_Cripto, insertar_transaccion

def Op5():
    """
    *	Mostrar todas las transacciones indicando fecha, moneda, tipo de operación, 
    *   código del usuario, cantidad y monto para el momento
    """    

    nombre_archivo = "Transacciones.txt"    

    mensaje = "Resumen de transacciones efectuadas a la fecha:"    
        
    print('-' * len(mensaje))
    print(mensaje)
    print('-' * len(mensaje))

    archivo = open(nombre_archivo,"r")    
    texto = archivo.read()

    """ import csv
    with open('Transacciones.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';',)        
        for row in spamreader:
            #print("Fecha: {}\n Moneda: {}\n Operación: {}\n Código de usuario: {}\n Cantidad: {}\n Monto en USD: {}".format(row[0], row[1], row[2],row[3], row[4], row[5]))
            print("Fecha: {} Moneda: {} Operación: {} ".format(row[0], row[1], row[2])) """
    
    print ("\n" + texto.replace("!","\n"))
    archivo.close()   
     
    input("\nPresione una tecla para volver al menú principal") 
