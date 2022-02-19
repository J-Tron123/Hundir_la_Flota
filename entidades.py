from winreg import HKEY_LOCAL_MACHINE
import numpy as np
from __init__ import *
import random

class Tablero():
    def __init__(self):
        pass

    def tablero(self):
        tablero = self.tablero = np.full(TABLERO, fill_value = " ")
        return tablero

class Barco():
    def __init__(self):
        pass

    def barco(self, tablero, lista):
        self.comprueba_casilla = []
        for i in lista:
            eslora = i[0]
            mayor = i[1]
            menor = i[2]
            medio = i[3]
            while True:
                orient = random.choice([VERTICAL, HORIZONTAL])
                fila_barco = random.randint(0,9)
                columna_barco = random.randint(0,9)
                if tablero[fila_barco, columna_barco] in self.comprueba_casilla:
                    fila_barco = random.randint(0,9)
                    columna_barco = random.randint(0,9)
                    orient = random.choice([VERTICAL, HORIZONTAL])
                    continue
                else:
                    if orient == VERTICAL:
                        if fila_barco >= mayor:
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=False) != False:
                                tablero[fila_barco - eslora + 1:fila_barco + 1, columna_barco] = "O"
                                break
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
                    elif orient == HORIZONTAL:
                        if columna_barco >= mayor:
                            if self.itera_casilla(eslora, fila_barco, columna_barco, orient, suma=False) != False:
                                tablero[fila_barco, columna_barco - eslora + 1:columna_barco + 1] = "O"
                                break
                            else:
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
        eslora += 1
        while not eslora == 0:
            if orient == VERTICAL:
                if suma == True:
                    if not [fila, columna] in self.comprueba_casilla:
                        self.comprueba_casilla.append([fila, columna])
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
            if x in range(0, 10) and y in range(0, 10):
                return (x, y)
            else: 
                return None
        except:
            print("Debes insertar números entre el 0 y el 9")
            self.coordenadas()
        
    def disparo_usuario(self, tablero_visible, tablero_invisible):
        tablero_invisible = tablero_invisible
        tablero_visible = tablero_visible
        coordenadas = self.coordenadas()
        if coordenadas:
            if tablero_invisible[coordenadas] == "O":
                print(f"Disparaste a {coordenadas} y acertaste")
                tablero_visible[coordenadas] = "X"
                return True
            elif tablero_visible[coordenadas] == "-":
                print(f"Ya disparaste a {coordenadas}")
                self.disparo_usuario(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)
            else:
                print(f"Disparaste a {coordenadas} y fallaste")
                tablero_visible[coordenadas] = "-"
                return False
        else:
            print("Debes insertar números entre el 0 y el 9")
            self.disparo_usuario(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)

    def disparo_maquina(self, tablero_visible, tablero_invisible):
        tablero_invisible = tablero_invisible
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