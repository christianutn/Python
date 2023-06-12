import campo
import os.path
import pickle
import random

def validar_rango(mens, inf, sup):
    n = int(input(mens))
    while n < inf or n > sup:
        print('-'*65)
        print('Error, el número a ingresar debes estar en el rango de [', inf, ', ', sup, ']...')
        n = int(input(mens))
    return n

def convertir_en_registro(vec):
    confederacion = int(vec[0])
    nombre = vec[1]
    puntos = int(vec[2])
    campeonatos = int(vec[3])
    registro = campo.Pais(confederacion, nombre, puntos, campeonatos)
    return registro

def add_in_order(vec, registro):
    izq, der = 0, len(vec)-1
    pos = 0
    while izq <= der:
        c = (izq + der)//2
        if registro.puntos == vec[c].puntos:
            pos = c

        if registro.puntos < vec[c].puntos:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [registro]


def generar_vec(nomb_archivo):
    m = open(nomb_archivo, 'rt')
    linea = m.readline()
    vec = []
    while linea != '':
        linea = linea[:len(linea)-1]
        vec_split = linea.split(',')
        registro = convertir_en_registro(vec_split)
        add_in_order(vec, registro)
        linea = m.readline()
    m.close()
    return vec

def mostrar_v_paises(vec):
    print('{:^13} | {:^30} | {:^6} | {:^7}'.format('Confederación', 'Nombre del País', 'Puntos', 'Campeón'))
    print('-'*65)
    for pais in vec:
        campo.to_string(pais)
    print('-'*65)


def menu():
    print()
    print('Menú de opciones: \n')
    print('1. Mostrar el listado completo de países.')
    print('2. Informar cuál es el país con mayor cantidad de campeonatos ganados.')
    print('3. Mostrar campeonatos ganados por paises de cada confederación.')
    print('4. Generar un nuevo vector conteniendo los países de una confederación X que se ingresa por teclado, y luego generar un archivo.')
    print('5. Ingresar una confederación por teclado y buscar su archivo de clasificación. ')
    print('6. Preparar el fixture del próximo mundial')
    print('7. Buscar en el fixture realizado en el ítem anterior un país cuyo nombre se ingresa por teclado')
    print('8. Terminar.')
    return validar_rango('Ingrese la opción correspondiente: ', 1, 8)

def may_campeon(vec):
    vec_campeon = []
    mayor = None
    for pais in vec:
        if mayor is None:
            mayor = pais
        elif pais.campeonatos > mayor.campeonatos:
            mayor = pais
            vec_campeon = []
            vec_campeon.append(mayor)
        elif pais.campeonatos == mayor.campeonatos:
            vec_campeon.append(pais)
    return vec_campeon


def generar_vc(vec, contadores):
    vc = [0]*contadores
    for pais in vec:
        if pais.campeonatos > 0:
            vc[pais.confederacion] += 1
    return vc

def generar_v_confx(vec, conf_x):
    vec_confx = []
    for pais in vec:
        if pais.confederacion == conf_x:
            nombre = pais.nombre
            puntos = pais.puntos
            campeonatos = pais.campeonatos
            registro = campo.Confederacion(nombre, puntos, campeonatos)
            add_in_order(vec_confx, registro)
    return vec_confx

def generar_archivo_b(nomb_archivo, vec_conf):
    fd = nomb_archivo
    m = open(fd, 'wb')
    for pais in vec_conf:
        pickle.dump(pais, m)
    m.flush()
    m.close()

def elegir_confederacion(mens='Es necesario que elija el código de confederación para crear archivo (“clasificacionX.dat”):\n'):
    print('-'*50)
    print(mens)
    print('0. UEFA')
    print('1. CONMEBOL')
    print('2. CONCACAF')
    print('3. CAF')
    print('4. AFC')
    print('5. OFC')
    return validar_rango('Elija la opción según corresponda: ', 0, 5)

def mostrar_arch_b(nomb_archivo):
    m = open(nomb_archivo, 'rb')
    tbm = os.path.getsize(nomb_archivo)
    print('-'*50)
    print('{:^30} | {:^6} | {:^7}'.format('Nombre del país', 'Puntos', 'Campeón'))
    print('-'*50)
    while m.tell() < tbm:
        registro = pickle.load(m)
        campo.to_string_conf(registro)
    print('-'*50)
    m.close()

def gestion_archivo(vec, cod_conf):
    fd_bin = 'clasificacion' + str(cod_conf) + '.dat'
    v_confx = generar_v_confx(vec, cod_conf)
    generar_archivo_b(fd_bin, v_confx)
    return fd_bin, len(v_confx)

def generar_matriz(fila, columna):
    matriz = []
    for i in range(fila):
        matriz.append([None]*columna)
    return matriz

def buscar_nomb_pais(vec, nomb_pais):
    pos = -1
    for i in range(len(vec)):
        if vec[i].nombre.lower() == nomb_pais.lower():
            pos = i
            break
    return pos

def validar_nomb_pais(vec, mens):
    nomb_pais = input(mens)
    pos = buscar_nomb_pais(vec, nomb_pais)
    while pos == -1:
        print('-'*65)
        print('El país ingresado no existe, vuelva a intentar...')
        nomb_pais = input(mens)
        pos = buscar_nomb_pais(vec, nomb_pais)


    return nomb_pais, pos

def ordenar_competidores(vec, pos_org):
    v_temp = vec[:]
    del v_temp[pos_org]
    v_temp[0:0] = [vec[pos_org]]
    return v_temp[:36]

def sortear(competidores):
    pos = random.randrange(8, len(competidores))
    pais = competidores[pos].nombre
    del competidores[pos]
    return pais


def cargar_fixture(matriz, vec, pos_org):
    competidores = ordenar_competidores(vec, pos_org)
    for i in range(1, len(matriz)):
        for j in range(len(matriz[0])):
            matriz[0][j] = competidores[j].nombre
            matriz[i][j] = sortear(competidores)

def conv_cod_grupo(cod):
    t_grupo = ('Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E', 'Grupo F', 'Grupo G', 'Grupo H')
    return t_grupo[cod]


def mostrar_fixture(matriz):
    print('-'*34)
    for j in range(len(matriz[0])):
        print('| {:^30} |'.format(conv_cod_grupo(j)))
        print('| {:^30} |'.format('-------'))

        for i in range(len(matriz)):
            print('| {:^30} |'.format(matriz[i][j]))
        print('-'*34)


def buscar_grupo(pais_x, matriz):
    grupo = -1
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if pais_x.lower() == matriz[i][j].lower():
                grupo = j
    return grupo




def main():
    fd = 'paises.csv'
    vec = generar_vec(fd)
    flags_matriz = False
    op = -1
    while op != 8:
        op = menu()
        if op == 1:
            print('-'*65)
            mostrar_v_paises(vec)
        elif op == 2:
            print('-'*65)
            vec_campeon = may_campeon(vec)
            if len(vec_campeon) == 1:
                print('El país con mayor cantidad de campeonatos del mundo es: \n')
                mostrar_v_paises(vec_campeon)
            else:
                print('Los países con mayor cantidad de campeonatos ganados del mundo son: \n')
                mostrar_v_paises(vec_campeon)
        elif op == 3:
            print('-'*72)
            print('Cantidad de paises que ganaron al menos un campeonato por confederación: \n')
            print('{:^13} | {:^28}'.format('Confederación', 'Cantidad de países campeones'))
            print('-'*45)
            vc = generar_vc(vec, 6)
            for i in range(len(vc)):
                print('{:^13} | {:^28}'.format(campo.convertir_cod_conf(i), vc[i]))
            print('-'*45)
        elif op == 4:
            fd_bin, cant_registros = gestion_archivo(vec, elegir_confederacion())
            print('-'*96)
            print('El archivo se generó de forma exitosa!!!')
            print('-'*96)
            print('Nombre del archivo:  "', fd_bin, '" - Cantidad de registros: ', cant_registros, sep='')
            print('-'*96)
            print('Datos del archivo: "', fd_bin, '"', sep='')
            mostrar_arch_b(fd_bin)
        elif op == 5:
            conf_x = elegir_confederacion()
            fd_x = 'clasificacion' + str(conf_x) + '.dat'
            if not os.path.exists(fd_x):
                print('-'*65)
                print('El archivo "', fd_x, '" no existe!', sep='')
                print('-'*65)
                print('Generando nuevo archivo...')
                fd_bin_nuevo, cant_r_nuevo = gestion_archivo(vec, conf_x)
                print('Se generó el archivo "', fd_x, '" de forma exitosa!!!', sep='')
                print('-'*50)
                cadena = 'Datos del archivo: ' + '"' + fd_x + '"'
                print('{:^50}'.format(cadena))
                mostrar_arch_b(fd_x)
            else:
                print('-'*50)
                cadena = 'Datos del archivo: ' + '"' + fd_x + '"'
                print('{:^50}'.format(cadena))
                mostrar_arch_b(fd_x)
        elif op == 6:
            print('-'*65)
            print('Preparar fixture del mundial: \n')
            pais_org, pos = validar_nomb_pais(vec, 'Ingrese nombre del país anfitrión: ')
            matriz = generar_matriz(4, 8)
            cargar_fixture(matriz, vec, pos)
            print('-'*39)
            print('EL Fixture fue generado exitosamente!!!')
            print('-'*39)
            print('Datos del fixture:\n')
            mostrar_fixture(matriz)
            flags_matriz = True
        elif op == 7:
            if flags_matriz:
                print('-'*65)
                print('Buscar país: \n')
                pais_x = input('Ingrese nombre del país a buscar: ')
                grupo = buscar_grupo(pais_x, matriz)
                if grupo != -1:
                    print('-'*65)
                    print('El país ', pais_x.capitalize(), ' pertenece: - ', conv_cod_grupo(grupo), ' -', sep='')
                else:
                    print('-'*65)
                    print('El país ', pais_x.capitalize(), ' no se encuentra registrado en el fixture...', sep='')
            else:
                print('-'*65)
                print('El fixture todavía no fue generado, ingrese a la opción número 6 primero.')

        elif op == 8:
            print('-'*65)
            print('Fin...')



if __name__ == '__main__':
  main()
