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
            while Disparo().disparo_usuario(tablero_invisible=maquina, tablero_visible=maquina_visible) == True:
                print(maquina_visible) # Hago el disparo del usuario
                for i in maquina_visible:
                    for j in i:
                        if j == "X":
                            dic_maquina["X"] += 1 # Verifico los aciertos del usuario
            print("dic_maquina", dic_maquina["X"])
            if dic_maquina["X"] >= 20:
                print("¡Enhorabuena! Ganaste") # Verifico si ganó el usuario
                break
            while Disparo().disparo_maquina(tablero_invisible=usuario, tablero_visible=usuario_visible) == True:
                print(usuario_visible) # Hago el disparo de la máquina
                for i in usuario_visible:
                    for j in i:
                        if j == "X":
                            dic_usuario["X"] += 1 # Verifivo los aciertos de la máquina
            print("dic_usuario", dic_usuario["X"])
            if dic_usuario["X"] >= 20:
                print("Ha ganado la máquina!") # Verifico si ganó la máquina
                break