import campo
import pickle
import os.path
import io
import random


def validar_rango(mens, inf, sup):
    n = int(input(mens))
    while n < inf or n > sup:
        print('-'*45)
        print('Error, el número ingresado se encuentra fuera del rango permitido...')
        n = int(input(mens))
    return n




def menu():
    print('-'*45)
    print('Menú de opciones: \n')
    print('1. Cargar arreglo.')
    print('2. Mostrar arreglo.')
    print('3. Buscar por ID.')
    print('4. Cantidad por tipo de aparato y pais de origen.')
    print('5. Generar archivo con registros cuyo precio sea menor al promedio.')
    print('6. Mostrar archivo.')
    print('7. Finalizar')
    return validar_rango('Ingrese la opción correspondiente: ', 1, 8)


def validar_inf(mens, inf):
    n = int(input(mens))
    while n < inf:
        print('-'*45)
        print('Error, el número ingresado no puede ser menor a ', inf, '.', sep='')
        n = int(input(mens))
    return n


def carga_aleatoria():
    t_prod = ('Televisor', 'Celular', 'Exprimidor', 'Notebook', 'Heladera', 'Freezer', 'Microondas', 'Licuadora',
              'Impresora', 'Calculadora', 'Rayador', 'Auricular', 'Memoria', 'Parlante', 'Cargador', 'Mouse', 'Teclado',
              'Lavarropas', 'Secadoras', 'Lavavajillas')
    id = random.randint(1000, 9999)
    nombre = random.choice(t_prod) + str(id)
    precio = round(random.uniform(100, 100000), 2)
    aparato = random.randint(0, 49)
    pais = random.randint(0, 19)
    registro = campo.Aparato(id, nombre, precio, aparato, pais)
    return registro


def add_in_order(vec, registro):
    izq, der = 0, len(vec) - 1
    pos = 0
    while izq <= der:
        c = (izq + der)//2
        if vec[c].precio == registro.precio:
            pos = c
            break
        elif vec[c].precio > registro.precio:
            der = c-1
        else:
            izq = c+1
    if izq > der:
        pos = izq

    vec[pos:pos] = [registro]



def generar_vec(n):
    vec = []
    for i in range(n):
        registro = carga_aleatoria()
        add_in_order(vec, registro)
    return vec

def imprimir_cabecera():
    cadena = '{:^4} | {:^15} | {:^8} | {:^7} | {:^4}'.format('ID', 'Nombre', 'Precio', 'Aparato', 'País')
    print(cadena)


def mostrar_vec(vec):
    imprimir_cabecera()
    for art in vec:
        campo.Aparato.to_string(art)


def sort_sec(vec, id):
    pos = -1
    for i in range(len(vec)):
        if vec[i].id == id:
            pos = i
            break
    return pos


def generar_matriz(fila, columna):
    matriz = [0]*fila
    for i in range(fila):
        matriz[i] = [0]*columna
    return matriz


def cargar_matriz_contadores(matriz, vec):
    for art in vec:
        matriz[art.aparato][art.pais] += 1


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != 0:
                print('Tipo de aparato: ', i, ' - País de origen: ', j, ' - Cantidad: ', matriz[i][j])


def promedio(vec):
    prom = 0
    ac = 0
    for art in vec:
        ac += art.precio

    prom = ac/len(vec)
    return prom


def crear_archivo(vec, fd, prom):
    m = open(fd, 'wb')
    for art in vec:
        if art.precio < prom:
            pickle.dump(art, m)
    m.flush()
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print('-'*45)
        print('El archivo no existe!!!')
        return

    m = open(fd, 'rb')
    tbm = os.path.getsize(fd)
    imprimir_cabecera()
    while m.tell() < tbm:
        linea = pickle.load(m)
        campo.Aparato.to_string(linea)



def test():
    fd = 'articulos.dat'
    flags_vec = False
    op = -1
    while op != 8:
        op = menu()

        if op == 1:
            print('-'*45)
            n = validar_inf('Ingrese cantidad de datos a cargar: ', 1)
            vec = generar_vec(n)
            print('-'*45)
            print('Arreglo generado de forma exitosa!!!')
            flags_vec = True
        elif flags_vec:
            if op == 2:
                print('-'*45)
                print('Datos del arreglo:\n')
                mostrar_vec(vec)
            elif op == 3:
                print('-'*45)
                print('Buscar por ID:\n')
                id = validar_rango('Ingrese id a buscar: ', 1000, 9999)
                pos = sort_sec(vec, id)
                print('-'*45)
                if pos == -1:
                    print('El id ingresado no existe!!!')
                else:
                    print('Id encontrado:\n')
                    campo.Aparato.to_string(vec[pos])
            elif op == 4:
                print('Cantidad por tipo de aparato y país de origen:\n')
                matriz = generar_matriz(50, 20)
                cargar_matriz_contadores(matriz, vec)
                mostrar_matriz(matriz)
            elif op == 5:
                print('-'*45)
                prom = promedio(vec)
                print('Crear archivo con registros cuyo precio sea menor al promedio: ', round(prom, 2))
                print()
                crear_archivo(vec, fd, prom)
                print('Archivo generado de forma exitosa!!!')
            elif op == 6:
                print('-'*45)
                print('Datos del archivo: ', fd)
                print()
                mostrar_archivo(fd)
            elif op == 7:
                print('-'*45)
                print('Fin...')

        else:
            print('-'*45)
            print('Primero es necesario generar el arreglo, ingrese a la opción número 1.')



test()
