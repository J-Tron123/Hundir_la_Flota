from entidades import Tablero, Barco, Disparo
from __init__ import *

class Game():
    def __init__(self):
        pass

    def partida(self):
        # Creo los tableros
        usuario = Tablero().tablero()
        maquina = Tablero().tablero()

        usuario_visible = Tablero().tablero()
        maquina_visible = Tablero().tablero()
        # Instancio los barcos de cada tablero y la lista de barcos de cada jugador
        Barco().barco(usuario, BARCOS)
        Barco().barco(maquina, BARCOS)

        print("Usuario", usuario_visible)
        print("\t")
        print("Máquina", maquina_visible)

        # Creo la forma de ruptura del bucle
        dic_usuario = {"X" : 0}
        dic_maquina = {"X" : 0}

        while True:
            for i in usuario_visible:
                for j in i:
                    if j == "X":
                        dic_usuario["X"] += 1
            for i in maquina_visible:
                for j in i:
                    if j == "X":
                        dic_maquina["X"] += 1
            if dic_usuario["X"] == 20:
                print("Ha ganado la máquina!")
                break
            elif dic_maquina["X"] == 20:
                print("¡Enhorabuena! Ganaste")
                break
            else:
                    while Disparo().disparo_usuario(tablero_invisible=maquina, tablero_visible=maquina_visible) == True:
                        print(maquina_visible)
                    while Disparo().disparo_maquina(tablero_invisible=usuario, tablero_visible=usuario_visible) == True:
                        print(usuario_visible)
