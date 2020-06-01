"""
    @author: Jorge Garrone
    Opcion3.py:
        Funciones para la opción 3 del sistema de Criptomonedas
"""
import requests
from Funciones import es_moneda, get_precio, obtener_cantidad_Cripto


def Op3():
    """
    *	Solicitar la moneda a mostrar
    *	Validar existencia de la moneda.
    *	Mostrar nombre de la moneda, cantidad y monto en USD para ese momento
    """  
    crypto=""
    while not es_moneda(crypto):
        crypto = input("Ingrese el nombre de la criptomoneda a consultar saldo: ")
    
    data = get_precio(crypto+"USDT").json()

    nombre_archivo = "Criptomonedas.txt"

    cantCrypto = obtener_cantidad_Cripto(nombre_archivo, crypto)
                
    cotiUSD = data["price"]
            
    total = float(cantCrypto) * float(cotiUSD)       
    
    print("\nResumen de datos:\n")
    
    print("Moneda: " + crypto)
    print("Cantidad en billetera: " + cantCrypto)
    print("El precio de la moneda " + crypto + " en dólares es: USD " + data["price"])
    print("Total acumulado es: USD " + str(total))    

    input("\nPresione una tecla para volver al menú principal") 