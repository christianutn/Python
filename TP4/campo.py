import random
class Pais():
    def __init__(self, confederacion, nombre, puntos, campeonatos):
        self.confederacion = confederacion
        self.nombre = nombre
        self.puntos = puntos
        self.campeonatos = campeonatos


def to_string(pais):
    cadena = '{:^13} | {:^30} | {:^6} | {:^7}'.format(convertir_cod_conf(pais.confederacion), pais.nombre, pais.puntos, pais.campeonatos)
    print(cadena)

def convertir_cod_conf(cod):
    t_conf = ('UEFA', 'CONMEBOL', 'CONCACAF', 'CAF', 'AFC', 'OFC')
    return t_conf[cod]

class Confederacion():
    def __init__(self, nombre, puntos, campeonatos):
        self.nombre = nombre
        self.puntos = puntos
        self.campeonatos = campeonatos


def to_string_conf(pais):
    cadena = '{:^30} | {:^6} | {:^7}'.format(pais.nombre, pais.puntos, pais.campeonatos)
    print(cadena)


