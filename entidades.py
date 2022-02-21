from winreg import HKEY_LOCAL_MACHINE
import numpy as np
from __init__ import *
import random

class Tablero():
    def __init__(self):
        pass

    def tablero(self):
        tablero = self.tablero = np.full(TABLERO, fill_value = " ") # Lleno los tableros de espacio vacíos
        return tablero

class Barco():
    def __init__(self):
        pass

    def barco(self, tablero, lista):
        self.comprueba_casilla = [] # Lista para guardar posiciones ya utilizadas
        for i in lista: # Recorro la lista de las medidas de los barcos que tiene la cantidad de medidas para la cantidad de barcos
            eslora = i[0]
            mayor = i[1]
            menor = i[2]
            medio = i[3]
            while True:
                orient = random.choice([VERTICAL, HORIZONTAL]) # Genero la posición de cada barco
                fila_barco = random.randint(0,9)
                columna_barco = random.randint(0,9)
                if tablero[fila_barco, columna_barco] in self.comprueba_casilla: # Si ya existe uno en la posición generada
                    fila_barco = random.randint(0,9)                             # crea una nueva posición
                    columna_barco = random.randint(0,9)
                    orient = random.choice([VERTICAL, HORIZONTAL])
                    continue
                else:
                    if orient == VERTICAL:      # Si es vertical pasa a condiciones para guardar las casillas que se van a
                        if fila_barco >= mayor: # generar y que no se salga del mapa
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=False) != False:
                                tablero[fila_barco - eslora + 1:fila_barco + 1, columna_barco] = "O"
                                break           # Si ya existe vuelve a iterar, si no existe rompe el bucle
                            else:
                                continue
                        elif fila_barco <= menor:
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=True) != False:
                                tablero[fila_barco:fila_barco + eslora, columna_barco] = "O"
                                break
                            else:
                                continue
                        elif (fila_barco > menor) and (fila_barco <= medio):
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=True) != False:
                                tablero[fila_barco:fila_barco + eslora, columna_barco] = "O"
                                break
                            else:
                                continue
                    elif orient == HORIZONTAL:     # Si es horizontal pasa a condiciones para guardar las casillas que se van a
                        if columna_barco >= mayor: # generar y que no se salga del mapa
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=False) != False:
                                tablero[fila_barco, columna_barco - eslora + 1:columna_barco + 1] = "O"
                                break
                            else:                  # Si ya existe vuelve a iterar, si no existe rompe el bucle
                                continue
                        elif columna_barco <= menor:
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=True) != False:
                                tablero[fila_barco, columna_barco:columna_barco + eslora] = "O"
                                break
                            else:
                                continue
                        elif (columna_barco > menor) and (columna_barco <= medio):
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=True) != False:
                                tablero[fila_barco, columna_barco:columna_barco + eslora] = "O"
                                break
                            else:
                                continue

    def itera_casilla(self, eslora, fila, columna, orient, suma=True):
        eslora += 1 # Aumento 1 la eslora para que no hayan barcos unidos en proa
        while not eslora == 0:
            if orient == VERTICAL:
                if suma == True:
                    if not [fila, columna] in self.comprueba_casilla:  # Verifico que en la posición no exista barco, si existe
                        self.comprueba_casilla.append([fila, columna]) # retorna False y hace que se rompa el bucle de arriba
                        fila += 1
                        eslora -= 1
                    else:
                        return False
                elif suma == False:
                    if not [fila, columna] in self.comprueba_casilla:
                        self.comprueba_casilla.append([fila, columna])
                        fila -= 1
                        eslora -= 1
                    else:
                        return False
            elif orient == HORIZONTAL:
                if suma == True:
                    if not [fila, columna] in self.comprueba_casilla:
                        self.comprueba_casilla.append([fila, columna])
                        columna += 1
                        eslora -= 1
                    else:
                        return False
                elif suma == False:
                    if not [fila, columna] in self.comprueba_casilla:
                        self.comprueba_casilla.append([fila, columna])
                        columna -= 1
                        eslora -= 1
                    else:
                        return False

class Disparo():
    def __init__(self):
        pass

    def coordenadas(self):
        x = input("Inserte el número de la fila a la que desea disparar: ")
        y = input("Inserte el número de la columna a la que desea disparar: ")
        try:
            x = int(x)
            y = int(y)
            if x in range(0, 10) and y in range(0, 10): # Valido que los datos ingresados cumplan lo necesario para hacer
                return (x, y)                           # el disparo de forma efectiva
            else: 
                return None
        except:
            print("Debes insertar números entre el 0 y el 9") # Si no lo cumplen vuelve a pedir datos
            self.coordenadas()
        
    def disparo_usuario(self, tablero_visible, tablero_invisible):
        tablero_invisible = tablero_invisible # Guardo cada tablero en una variable
        tablero_visible = tablero_visible
        coordenadas = self.coordenadas()
        if coordenadas:
            if tablero_invisible[coordenadas] == "O":            # Si en el invisible hay barco en las coordenadas ingresadas
                print(f"Disparaste a {coordenadas} y acertaste") # pone X en el visible
                tablero_visible[coordenadas] = "X"
                return True
            elif tablero_visible[coordenadas] == "-":         # Si ya hay - es que ya disparaste allí y te pide nuevas coordenadas
                print(f"Ya disparaste a {coordenadas}")
                self.disparo_usuario(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)
            else:
                print(f"Disparaste a {coordenadas} y fallaste")  # Si en el invisible no hay barco en las coordenadas ingresadas
                tablero_visible[coordenadas] = "-"               # pone - en el visible
                return False
        else:
            print("Debes insertar números entre el 0 y el 9")
            self.disparo_usuario(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)

    def disparo_maquina(self, tablero_visible, tablero_invisible): # La misma lógica del disparo del usuario pero generando
        tablero_invisible = tablero_invisible                      # las coordenadas aleatoriamente
        tablero_visible = tablero_visible
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        coordenadas = (x, y)
        if tablero_invisible[coordenadas] == "O":
            print(f"La máquina disparó a {coordenadas} y acertó")
            tablero_visible[coordenadas] = "X"
            return True
        elif tablero_visible[coordenadas] == "-":
            self.disparo_maquina(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)
        else:
            print(f"La máquina disparó a {coordenadas} y falló")
            tablero_visible[coordenadas] = "-"
            return False