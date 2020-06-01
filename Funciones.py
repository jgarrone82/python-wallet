"""
    @author: Jorge Garrone
    Funciones.py:
        Funciones comunes para el sistema de Criptomonedas
"""
import requests
import time

def get_precio(cryptoMoneda):
    '''Funcion que se conecta a la API de Binance para buscar el valor de una criptomoneda en USD'''
    return requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+cryptoMoneda)

def es_numero(numero): 
    '''Funcion que verifica que el valor ingresado sea un número'''
    return numero.replace('.','',1).isdigit()

def es_moneda(cryptoMoneda):
    '''Funcion que verifica que el valor ingresado sea una criptomoneda '''
    criptos = ["BTC","LTC","ETH"]
    if cryptoMoneda in criptos:
        return True
    else:        
        return False

def es_mi_codigo(codigo):
    '''Funcion que valida si el código ingresado pertenece al usuario '''
    mi_codigo = ["1kJmKcDTE2"]
    return codigo in mi_codigo

def actualizar_dato(archivo,buscar,reemplazar):
	"""
	Función cambia una linea entera de un archivo
	Tiene que recibir el nombre del archivo, la cadena a buscar,
    y la cadena a reemplazar si la linea coincide con buscar
	"""
 
	with open(archivo, "r") as f:
		# obtenemos las lineas del archivo en una lista
		lines = (line.rstrip() for line in f)
 
		# busca en cada linea si existe la cadena a buscar, y si la encuentra
		# la reemplaza
		altered_lines = [reemplazar if line==buscar else line for line in lines]
 
	with open(archivo, "w") as f:
		# guarda nuevamente todas las lineas en el archivo
		f.write('\n'.join(altered_lines) + '\n')

def obtener_cantidad_Cripto(nombre_archivo,crypto):
    """"
    Función obtiene la cantidad de una criptomoneda
    """    
    #Abro el archivo para leer los datos
    archivo = open(nombre_archivo,"r")    
    texto = archivo.read()
    archivo.close()
    #Separo las lineas en un objeto lista
    lineas = texto.splitlines()    
    #Creo un diccionario y le asigno los valores de nombre de moneda
    # y la cantidad de la misma
    diccionario={}
    for linea in lineas:
        termino = linea.split(":")        
        diccionario[termino[0]]=termino[1]
    #Retorno el valor encontrado de cantidad para la moneda elegida   
    return diccionario.get(crypto) 

def insertar_transaccion(cripto, operacion, codigo_user, cantCripto, cotiUSD):
    """
    Función que inserta en el archivo de transacciones un movimiento de criptomoneda
    # indicando fecha, moneda, tipo de operación, código del usuario, 
    # cantidad y monto para el momento.
    """
    nombre_archivo = "Transacciones.txt"
    #Abro el archivo para escribir la nueva transacción
    archivo = open(nombre_archivo,"a")
    archivo.write("\n" + "Fecha: " + time.strftime("%c") + " ! Moneda: " + cripto + " ! Operación: " + operacion + " ! Código de usuario: " + codigo_user + " ! Cantidad: " + cantCripto + " ! Monto en USD: " + cotiUSD + " !" )        
    archivo.close()