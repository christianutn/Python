import random
class Participante():
    def __init__(self, nom, continente, ranking):
        self.nombre = nom
        self.continente = continente
        self.ranking = ranking

class Resultado():
    def __init__(self, equipo1, puntos1, equipo2, puntos2):
        self.equipo1 = equipo1
        self.puntos1 = puntos1
        self.equipo2 = equipo2
        self.puntos2 = puntos2

def cargar_vr_aleat(vec_r, vec_compet):
    for i in range(len(vec_r)):
        hay_empate = True
        while hay_empate:
            p1 = random.randint(0, 100)
            p2 = random.randint(0, 100)
            equipo1 = vec_compet[i].nombre
            puntos1 = p1
            equipo2 = vec_compet[-i-1].nombre
            puntos2 = p2
            if p1 != p2:
                vec_r[i] = Resultado(equipo1, puntos1, equipo2, puntos2)
                hay_empate = False

def cargar_vr_manual(vec_r, vec_compet):
     for i in range(len(vec_r)):
        hay_empate = True
        while hay_empate:
            print('-'*80)
            p1 = validar_inf('Cantidad de puntos obtenidos por ' + vec_compet[i].nombre + ': ', 1)
            p2 = validar_inf('Cantidad de puntos obtenidos por ' + vec_compet[-i-1].nombre + ': ', 1)
            equipo1 = vec_compet[i].nombre
            puntos1 = p1
            equipo2 = vec_compet[-i-1].nombre
            puntos2 = p2
            if p1 != p2:
                vec_r[i] = Resultado(equipo1, puntos1, equipo2, puntos2)
                hay_empate = False
            else:
                print('-'*80)
                print('Fue empate!!! Cargue los nuevos resultados...')


def cargar_vec_aleatoria(vec):
    l_participante = ['Juan', 'Pedro', 'Martin', 'Eric', 'Rosa', 'Maria', 'Raul', 'Jaime', 'Joel', 'Marta', 'Miguel', 'Agusto', 'Tomas', 'Sol', 'Flor', 'David']
    l_ranking = list(range(1, 100))
    for i in range(len(vec)):
        nombre = random.choice(l_participante)
        l_participante = remover_elemento(l_participante, nombre)
        continente = random.randint(0, 4)
        ranking = random.choice(l_ranking)
        l_ranking = remover_elemento(l_ranking, ranking)
        vec[i] = Participante(nombre, continente, ranking)


def cargar_vec_manual(vec):
    print('Cargar datos:')
    for i in range(len(vec)):
        print('-'*80)
        print('Registro nro', i+1)
        nombre = validar_nombre(input('Ingrese nombre:'), vec)
        continente = validar_rango('Continente - 0. América - 1. Europa - 2. Asia - 3. África - 4. Oceanía: ', 0, 4)
        ranking = validar_ranking(validar_inf('Ranking Mundial: ', 1), vec)
        vec[i] = Participante(nombre, continente, ranking)


def validar_inf(mens, inf):
    n = int(input(mens))
    while n < inf:
        print('-'*80)
        print('Error, se debe ingresar un número mayor o igual a ', inf, '.')
        n = int(input(mens))
    return n

def validar_rango(mens, inf, sup):
    n = int(input(mens))
    while n < inf or n > sup:
        print('-'*80)
        print('Error, el número a ingresar debe estar en el rango [', inf, ', ', sup, ']...', sep='')
        n = int(input(mens))
    return n


def validar_nombre(nom, vec):
    while existe_nom(nom, vec):
        print('-'*80)
        print('El nombre ya existe...')
        nom = input('Ingrese nombre: ')
    return nom

def validar_ranking(ranking, vec):
    while existe_ranking(ranking, vec):
        print('-'*80)
        print('Ranking ya existe...')
        ranking = validar_inf('Ingrese ranking: ', 1)
    return ranking


def mostrar_enfrentamientos(vr):
    r = ''
    for res in vr:
        r += '{:>15}'.format(res.equipo1 + ': ' + str(res.puntos1))
        r += '{:>15}'.format('Vs.')
        r += '{:>15}'.format(res.equipo2 + ': ' + str(res.puntos2))
        r += '\n'
    return r

def mostrar_cruces(vc):
    r = ''
    for i in range(len(vc)//2):
        r += '{:>15}'.format(vc[i].nombre)
        r += '{:>15}'.format('Vs.')
        r += '{:>15}'.format(vc[-i-1].nombre)
        r += '\n'

    return r

def mostrar_datos(vc):
    r = ''
    for participante in vc:
        r += '{:<30}'.format('Nombre: ' + str(participante.nombre))
        r += '{:<30}'.format('Continente: ' + str(participante.continente))
        r += '{:<30}'.format('Ranking: ' + str(participante.ranking))
        r += '\n'
    return r


def mostrar_continente(v_contadores, tupla):
    r = ''
    for i in range(len(v_contadores)):
        if v_contadores[i] != 0:
             r += '{:<10}'.format(tupla[i] + ':' + str(v_contadores[i]) + ' - ')
    return r

def mostrar_podio(campeon, segundo, tercero):
    print('Podio:\n')
    print('Campeón: ', campeon[0].nombre)
    print('Segundo: ', segundo[0].nombre)
    print('Tercero: ', tercero[0].nombre)



def existe_nom(nom, vec):
    existe = False
    for n in vec:
        if n is not None and n.nombre == nom:
            existe = True
    return existe


def existe_ranking(ranking, vec):
    existe = False
    for r in vec:
        if r is not None and r.ranking == ranking:
            existe = True
    return existe



def remover_elemento(lista, elemento):
    posic = 0
    for elem in lista:
        if elem == elemento:
            break
        posic += 1
    del lista[posic]
    return lista


def ordenar(vec):
    for i in range(len(vec)-1):
        for j in range(i+1, len(vec)):
            if vec[i].ranking < vec[j].ranking:
                vec[i], vec[j] = vec[j], vec[i]


def vc_contadores(vec, contadores):
    vc = [0]*contadores
    for participante in vec:
        ind = participante.continente
        vc[ind] += 1
    return vc


def generar_vg(vr, vc):
    vg = [None]*(len(vc)//2)
    for i in range(len(vg)):
        if vr[i].puntos1 > vr[i].puntos2:
            vg[i] = vc[i]
        else:
            vg[i] = vc[-i-1]
    return vg


def generar_vr(vc, tipo_de_carga):
    v_res = [None]*(len(vc)//2)
    if tipo_de_carga == 1:
        cargar_vr_aleat(v_res, vc)
    elif tipo_de_carga == 2:
        cargar_vr_manual(v_res, vc)
    return v_res


def promedio_ptje(vr):
    prom = 0
    ac = 0
    for res in vr:
        ac += res.puntos1 + res.puntos2
    prom = ac/(len(vr)*2)
    return prom



def incrementar_ranking(participante, incremento):
    participante.ranking += incremento

def cargar_datos(mens):
    print('-'*80)
    print(mens)
    print()
    print('1. Carga aleatoria.')
    print('2. Carga Manual.')
    op = validar_rango('Ingrese la opción correspondiente: ', 1, 2)
    return op


def menu():
    print('Menú de opciones: ')
    print('1. Mostrar datos de los 16 participantes ordenados por ranking y la cantidad de participantes por continente.')
    print('2. Mostrar cruces, resultados y ganadores de octavos; y puntaje promedio por participante.')
    print('3. Mostrar cruces, resultados y ganadores de cuartos; y puntaje promedio por participante.')
    print('4. Mostrar cruces, resultados y ganadores de semis; y puntaje promedio por participante.')
    print('5. Mostrar cruce, resultado y ganador de la final; y podio final.')
    print('6. Incrementar ranking - +25 para el primero - +15 para el segundo - +5 para el tercero; y mostrar participantes ordenados por ranking.')
    print('7. Terminar.')
    op = validar_rango('Ingrese la opción correspondiente: ', 1, 7)
    return op


def generar_vc_inicial(mens):

    carga = cargar_datos(mens)
    if carga == 1:
        vc = [None]*16
        cargar_vec_aleatoria(vc)

    else:
        vc = [None]*16
        cargar_vec_manual(vc)
    return vc

def op2(vc, v_contadores):
    ordenar(vc)
    print('-'*80)
    print('Datos de los 16 participantes iniciales:')
    d_16 = mostrar_datos(vc)
    print(d_16)
    print('-'*80)
    print('Cantidad de participantes por continente:')
    t_continente = ('América', 'Europa', 'Asia', 'África', 'Oceanía')
    d_continente = mostrar_continente(v_contadores, t_continente)
    print(d_continente)

def resultado(vc, mens, m_prom=True):

    print('-'*80)
    print('Cruces:', mens)
    print()
    d_cruce = mostrar_cruces(vc)
    print(d_cruce)

    carga = cargar_datos('¿Como de sea realizar la carga de resultados?: ' + mens)
    vr = generar_vr(vc, carga)

    print('-'*80)
    print('Resultados:', mens)
    print()
    d_res = mostrar_enfrentamientos(vr)
    print(d_res)

    vg = generar_vg(vr, vc)
    print('-'*80)
    print('Ganadores:', mens)
    print()
    d_gan = mostrar_datos(vg)
    print(d_gan)

    prom = promedio_ptje(vr)
    if m_prom:
        print('-'*80)
        print('Promedio de puntos por participante:', round(prom, 2))

    return vg, vr, prom

def generar_v_perdedores(vg, vg_anterior):
    v_perd = []
    for i in range(len(vg_anterior)):
        if not vg_anterior[i] in vg:
            v_perd.append(vg_anterior[i])
    return v_perd


def op3(vc_16):
    vg, vr, prom = resultado(vc_16, 'Octavos')
    return vg, vr, prom


def op4(vg_8):
    vg, vr, prom = resultado(vg_8, 'Cuartos')
    return vg, vr, prom

def op5(vg_4):
    vg, vr, prom = resultado(vg_4, 'Semifinales')
    return vg, vr, prom

def solo_mostrar(vc, vr, prom, m_prom = True):
    print(mostrar_cruces(vc))
    print(mostrar_enfrentamientos(vr))
    if m_prom:
        print('Promedio:', prom)


def buscar_incr_ranking(vc_final, ranking, incremento):
    izq = 0
    der = len(vc_final)-1

    while izq <= der:
        c = (izq + der)//2
        if vc_final[c].ranking == ranking:
            vc_final[c].ranking += incremento
            return

        if vc_final[c].ranking < ranking:
            der = c - 1
        else:
            izq = c + 1


def iniciar():

    print('{:<30}'.format('Sistema de Gestión de una Competencia'))
    print()
    vc_16 = generar_vc_inicial('¿Como desea realizar la cargar de datos de los participantes?')
    ordenar(vc_16)

    print('-'*80)
    print('Datos de los participantes\n')
    print(mostrar_datos(vc_16))

    print('-'*80)
    print('Comenzando carga de octavos de final...')
    vg_8, vr_16, prom_16 = resultado(vc_16, 'Octavos de final')

    print('-'*80)
    print('Comenzando carga de cuartos de final...')
    vg_4, vr_8, prom_8 = resultado(vg_8, 'Cuartos de final')

    print('-'*80)
    print('Comenzando carga de semifinales...')
    vg_2, vr_4, prom_4 = resultado(vg_4, 'Semifinales')

    print('-'*80)
    print('Comenzando carga de la final...')
    v_campeon, vr_final, prom_final = resultado(vg_2, 'Final', m_prom=False)
    v_segundo = generar_v_perdedores(v_campeon, vg_2)

    print('-'*80)
    print('Comenzando carga resultados por tercer y cuarto puesto...')
    vc_bronce = generar_v_perdedores(vg_2, vg_4)
    v_tercero, vr_tercero, prom_tercero = resultado(vc_bronce, 'Tercer - Cuarto , puesto', m_prom=False)

    print('-'*80)
    mostrar_podio(v_campeon, v_segundo, v_tercero)
    print('-'*80)
    print('Incrementando ranking...')
    print(v_campeon[0].nombre, ': +25')
    print(v_segundo[0].nombre, ': +15')
    print(v_tercero[0].nombre, ': +5')
    print('-'*80)
    print('Datos participantes con ranking actualizados\n')
    buscar_incr_ranking(vc_16, v_campeon[0].ranking, 25)
    buscar_incr_ranking(vc_16, v_segundo[0].ranking, 15)
    buscar_incr_ranking(vc_16, v_tercero[0].ranking, 5)
    print(mostrar_datos(vc_16))
    print('La carga fue completada, si desea puede repasar los resultados a través del siguiente menú de opciones...')
    print('-'*80)



iniciar()






