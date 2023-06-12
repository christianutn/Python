import random
# l_participante = ['Juan', 'Pedro', 'Martin', 'Eric', 'Rosa', 'Maria', 'Raul', 'Jaime', 'Joel', 'Marta', 'Miguel', 'Agusto', 'Tomas', 'Sol', 'Flor', 'David']

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
            p1 = validar('Cantidad de puntos obtenidos por ' + vec_compet[i].nombre + ': ', 1)
            p2 = validar('Cantidad de puntos obtenidos por ' + vec_compet[-i-1].nombre, 1)
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


def validar(mens, inf):
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


def cargar_vec(vec):
    print('Cargar datos:')
    for i in range(len(vec)):
        print('-'*60)
        print('Registro nro', i+1)
        nombre = validar_nombre(input('Ingrese nombre:'), vec)
        continente = validar_rango('Continente - 0. América - 1. Europa - 2. Asia - 3. África - 4. Oceanía: ', 0, 4)
        ranking = validar_ranking(validar('Ranking Mundial: ', 1), vec)
        vec[i] = Participante(nombre, continente, ranking)


def validar_nombre(nom, vec):
    while existe_nom(nom, vec):
        print('-'*80)
        print('El nombre ya existe...')
        nom = input('Ingrese nombre: ')
    return nom


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

def validar_ranking(ranking, vec):
    while existe_ranking(ranking, vec):
        print('-'*80)
        print('Ranking ya existe...')
        ranking = validar('Ingrese ranking: ', 1)
    return ranking


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


def mostrar_datos(participante):
    r = ''
    r += '{:<30}'.format('Nombre: ' + str(participante.nombre))
    r += '{:<30}'.format('Continente: ' + str(participante.continente))
    r += '{:<30}'.format('Ranking: ' + str(participante.ranking))
    return r

def vc_contadores(vec, contadores):
    vc = [0]*contadores
    for participante in vec:
        ind = participante.continente
        vc[ind] += 1
    return vc

def enfrentar(vr, vc):
    vg = [None]*(len(vc)//2)
    for i in range(len(vg)):
        if vr[i].puntos1 > vr[i].puntos2:
            vg[i] = vc[i]
        else:
            vg[i] = vc[-i-1]
    return vg




def promedio_ptje(registro_res):
    prom = 0
    ac = 0
    for res in registro_res:
        ac += res.puntos1 + res.puntos2
    prom = ac/(len(registro_res)*2)
    return prom



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
    print('-'*80)
    print('Menú de opciones: ')
    print('1. Cargar nuevos datos')
    print('2. Mostrar datos de los 16 participantes, la cantidad de participantes por continente y ordenadar por ranking.')
    print('3. Mostrar cruces, resultados y ganadores de octavos; y puntaje promedio por participante.')
    print('4. Mostrar cruces, resultados y ganadores de cuartos; y puntaje promedio por participante.')
    print('5. Mostrar cruces, resultados y ganadores de semis; y puntaje promedio por participante.')
    print('6. Mostrar cruce, resultado y ganador de la final; y podio final.')
    print('7. Incrementar ranking - +25 para el primero - +15 para el segundo - +5 para el tercero; y mostrar participantes ordenados por ranking.')
    print('8. Terminar.')
    op = validar_rango('Ingrese la opción correspondiente: ', 1, 8)
    return op


def generar_vr(vc, tipo_de_carga):
    v_res = [None]*(len(vc)//2)
    if tipo_de_carga == 1:
        cargar_vr_aleat(v_res, vc)
    elif tipo_de_carga == 2:
        cargar_vr_manual(v_res, vc)
    return v_res


def resultados(vec_comp, mens_instancia, mostrar_prom = True):
    print('-'*80)
    print('{:>35}'.format(mens_instancia))
    print()
    r = mostrar_cruces(vec_comp)
    print(r)
    print()
    carga = cargar_datos('¿Como desea realizar la carga de resultados? ')
    print('-'*80)
    vr = generar_vr(vec_comp, carga)

    print('{:>35}'.format('Resultados:'))
    print()

    res = mostrar_enfrentamientos(vr)
    print(res)
    print('-'*80)
    v_ganadorde16 = enfrentar(vr, vec_comp)
    print('{:>50}'.format('Ganadores resultantes:'))
    print()

    for ganadores in v_ganadorde16:
        r = mostrar_datos(ganadores)
        print(r)
    print('-'*80)
    prom = promedio_ptje(vr)
    if mostrar_prom:
        print('Promedio de puntos por participantes de los octavos de final:', round(prom, 2))


    return v_ganadorde16, vr, prom


def op1():
    carga = cargar_datos('¿Como desea realizar la carga de datos?')
    if carga == 1:
        vc_16 = [None]*16
        cargar_vec_aleatoria(vc_16)

    else:
        vc_16 = [None]*16
        cargar_vec(vc_16)
    return vc_16



def cod_cont(cod):
    codigo = None
    if cod == 0:
        codigo = 'América'
    elif cod == 1:
        codigo = 'Europa'
    elif cod == 2:
        codigo = 'Asia'
    elif cod == 3:
        codigo = 'África'
    elif cod == 4:
        codigo = 'Oceanía'
    return codigo

def op2(vec_comp, mostrar_cant_cont = True):
    vc = vc_contadores(vec_comp, 5)
    print('-'*80)
    print('Datos de los 16 participantes')
    print()
    for participante in vec_comp:
        r = mostrar_datos(participante)
        print(r)
    print()
    if mostrar_cant_cont:
        print('-'*80)
        print('Cantidad de participantes por continente: ')
        r = ''
        for i in range(len(vc)):
            if vc[i] != 0:
                r += '{:<10}'.format(cod_cont(i) + ':' + str(vc[i]) + ' - ')

        print(r)

    print('-'*80)

def op6(vc_final, vc_tercero):
    vg_final, vr, prom = resultados(vc_final, '- FINAL -', mostrar_prom=False)
    vr_tercero = generar_vr(vc_tercero, cargar_datos('¿Como va a cargar los resultados por tercer y cuarto puesto?'))
    vg_tercero = enfrentar(vr_tercero, vc_tercero)
    print('-'*80)
    print('Podio: ')
    print()
    print('Campeón: ', vg_final[0].nombre)
    v_segundo = []
    for i in range(len(vc_final)):
        if not vc_final[i] in vg_final:
            v_segundo.append(vc_final[i])
    print('Segundo: ', v_segundo[0].nombre)
    print('Tercero: ', vg_tercero[0].nombre)
    print('-'*80)
    return vg_final[0], v_segundo[0], vg_tercero[0]


def op7(campeon, segundo, tercero, vc_total, se_incr_ran):
    print('Se incrementó automaticamentes los ranking del podio:', campeon.nombre, '+25 -', segundo.nombre, '+15 -', tercero.nombre, '+5')
    if not se_incr_ran:
        incrementar_ranking(campeon, 25)
        incrementar_ranking(segundo, 15)
        incrementar_ranking(tercero, 5)
    print('-'*80)
    print('Nuevos datos, con ranking modificados y ordenados')
    vc_orde = vc_total[:]
    ordenar(vc_orde)
    op2(vc_orde, mostrar_cant_cont=False)


def solo_mostrar(vc, vr, prom, mens, mostrar_prom = True):
    print('-'*80)
    print('{:>35}'.format(mens))
    print()
    r = mostrar_cruces(vc)
    print(r)
    print()
    print('-'*80)
    print('{:>35}'.format('Resultados:'))
    print()
    res = mostrar_enfrentamientos(vr)
    print(res)
    print('-'*80)
    print('{:>50}'.format('Ganadores resultantes:'))
    print()
    vg = enfrentar(vr, vc)
    for ganadores in vg:
        r = mostrar_datos(ganadores)
        print(r)
    prom = promedio_ptje(vr)
    if mostrar_prom:
        print('-'*80)
        print('Promedio de puntos por participantes de los octavos de final:', round(prom, 2))

def mostrar_final(vc, vr, camp, seg, ter):
    solo_mostrar(vc, vr, 0, '- Final !!! -',  mostrar_prom=False)
    print('-'*80)
    print('Podio: ')
    print()
    print('Campeón: ', camp.nombre)
    print('Segundo: ', seg.nombre)
    print('Tercero: ', ter.nombre)




def test():
    print('{:<30}'.format('Sistema de Gestión de una Competencia'))
    print()
    vec_competidores = op1()
    ordenar(vec_competidores)
    op = menu()
    paso_octavos = False
    paso_cuartos = False
    paso_semis = False
    paso_final = False
    se_incr_ran = False


    while op != 8:
        if op == 1:
            vec_competidores = op1()
            ordenar(vec_competidores)
            paso_octavos, paso_cuartos, paso_semis, paso_final = False, False, False, False
            se_incr_ran = False
        elif op == 2:
            op2(vec_competidores)

        elif op == 3:
            if not paso_octavos:
                vg_octavos, vr_oct, prom_oct = resultados(vec_competidores, '- Octavos de final -')
                paso_octavos = True
            else:
                solo_mostrar(vec_competidores, vr_oct, prom_oct, '- Octavos de final -')


        elif op == 4:
            if not paso_octavos:
                print('-'*80)
                print('Todavía no se cargaron los resultados de los octavos de final...')
                print('Carguelos ahora...')
                vg_octavos, vr_oct, prom_oct = resultados(vec_competidores, ' - Octavos de final -')
                paso_octavos = True

            if not paso_cuartos:
                vg_cuartos, vr_cuart, prom_cuart = resultados(vg_octavos, '- Cuartos de final -')
                paso_cuartos = True
            elif paso_cuartos:
                solo_mostrar(vg_cuartos, vr_cuart, prom_cuart, '- Cuartos de final -')

        elif op == 5:
            if not paso_octavos:
                print('-'*80)
                print('Todavía no se cargaron los resultados de los octavos de final...')
                print('Carguelos ahora...')
                vg_octavos, vr_oct, prom_oct = resultados(vec_competidores, '- Octavos de final -')
                paso_octavos = True
            if not paso_cuartos:
                print('-'*80)
                print('Todavía no se cargaron los resultados de los cuartos de final...')
                print('Carguelos ahora...')
                vg_cuartos, vr_cuart, prom_cuart = resultados(vg_octavos, '- Cuartos de final -')
                paso_cuartos = True

            if not paso_semis:
                vg_semis, vr_semis, prom_semis = resultados(vg_cuartos, '- Semifinal -')
                paso_semis = True
            elif paso_semis:
                solo_mostrar(vg_semis, vr_semis, prom_semis, '- Semifinal -')
        elif op == 6:
            if not paso_octavos:
                print('-'*80)
                print('Todavía no se cargaron los resultados de los octavos de final...')
                print('Carguelos ahora...')
                vg_octavos, vr_oct, prom_oct = resultados(vec_competidores, '- Octavos de final -')
                paso_octavos = True
            if not paso_cuartos:
                print('-'*80)
                print('Todavía no se cargaron los resultados de los cuartos de final...')
                print('Carguelos ahora...')
                vg_cuartos, vr_cuart, prom_cuart = resultados(vg_octavos, '- Cuartos de final -')
                paso_cuartos = True
            if not paso_semis:
                print('-'*80)
                print('Todavía no se cargaron los resultados de la semifinal...')
                print('Carguelos ahora...')
                vg_semis, vr_semis, prom_semis = resultados(vg_cuartos, '- Semifinal -')
                paso_semis = True

            if not paso_final:
                vc_tercero = []
                for i in range(len(vg_cuartos)):
                    if not vg_cuartos[i] in vg_semis:
                        vc_tercero.append(vg_cuartos[i])
                campeon, segundo, tercero = op6(vg_semis, vc_tercero)
                paso_final = True
            elif paso_final:
                mostrar_final(vg_semis, vr_semis, campeon, segundo, tercero)

        elif op == 7:
            if not paso_octavos:
                print('-'*80)
                print('Todavía no se cargaron los resultados de los octavos de final...')
                print('Carguelos ahora...')
                vg_octavos, vr_oct, prom_oct = resultados(vec_competidores, '- Octavos de final -')
                paso_octavos = True
            if not paso_cuartos:
                print('-'*80)
                print('Todavía no se cargaron los resultados de los cuartos de final...')
                print('Carguelos ahora...')
                vg_cuartos, vr_cuart, prom_cuart = resultados(vg_octavos, '- Cuartos de final -')
                paso_cuartos = True
            if not paso_semis:
                print('-'*80)
                print('Todavía no se cargaron los resultados de la semifinal...')
                print('Carguelos ahora...')
                vg_semis, vr_semis, prom_semis = resultados(vg_cuartos, '- Semifinal -')
                paso_semis = True
            if not paso_final:
                vc_tercero = []
                for i in range(len(vg_cuartos)):
                    if not vg_cuartos[i] in vg_semis:
                        vc_tercero.append(vg_cuartos[i])
                campeon, segundo, tercero = op6(vg_semis, vc_tercero)
                paso_final = True
            if paso_final:
                op7(campeon, segundo, tercero, vec_competidores, se_incr_ran)
                se_incr_ran = True
        op = menu()


# NO TOCAAAAAAAAT
test()
