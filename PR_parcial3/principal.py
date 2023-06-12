import campo
import random


def validar_rango(mens, inf, sup):
    n = int(input(mens))
    while n < inf or n > sup:
        print('-'*45)
        print('Error, el número ingresado está fuera del rango permitido...')
        n = int(input(mens))
    return n


def menu():
    print('-'*45)
    print('Menú de opciones: \n')
    print('1. Cargar vector, y mostrar vector.')
    print('2. Mostrar datos cuyo importe supere a un valor x.')
    print('3. Mostrar importe total por cada actividad.')
    print('4. Mostrar datos del cliente con mayor precio para la actividad número 3.')
    print('5. Buscar por id.')
    print('6. Finalizar.')
    return validar_rango('Ingrese la opción correspondiente: ', 1, 6)


def validar_inf(mens, inf):
    n = int(input(mens))
    while n < inf:
        print('-'*45)
        print('Error, el número a ingresar no puede ser menor a ', inf, '.', sep='')
        n = int(input(mens))
    return n


def carga_aleatoria():
    t_apellidos = ('Bergero', 'Lopez', 'Gimenez', 'Benitez', 'Messi', 'Ronaldo', 'Otamendi', 'Quiroga', 'Zarabia', 'Riquelme',
                   'Armani', 'Tagliafico', 'Martinez', 'Lujambio', 'Sand', 'Ortigoza', 'Paredes', 'De Paul')
    id = random.randint(1000, 9999)
    apellido = random.choice(t_apellidos) + str(id)
    importe = round(random.uniform(1, 5000))
    actividad = random.randint(0, 18)
    registro = campo.Cliente(id, apellido, importe, actividad)
    return registro


def generar_vec(n):
    vec = []
    for i in range(n):
        registro = carga_aleatoria()
        vec.append(registro)
    return vec


def imprimir_cabecera():
    cadena = '{:^4} | {:^15} | {:^7} | {:^9}'.format('ID', 'Apellido', 'Importe', 'Actividad')
    print(cadena)



def mostrar_vec(vec):
    imprimir_cabecera()
    for cliente in vec:
        campo.Cliente.to_strign(cliente)


def mostrar_datos_importe(vec, importe):
    flags_existe = False
    for cliente in vec:
        if cliente.importe > importe:
            if not flags_existe:
                imprimir_cabecera()
            campo.Cliente.to_strign(cliente)
            flags_existe = True
    if not flags_existe:
        print('-'*45)
        print('No se registraron datos con un importe superior a $', importe, '.', sep='')


def generar_vc(vec, contadores):
    vc = [0]*contadores
    for cliente in vec:
        vc[cliente.actividad] += cliente.importe
    return vc


def mostrar_vc(vc):
    for i in range(len(vc)):
        if vc[i] != 0:
            print('Actividad: ', i, ' - Importe total: $', vc[i])


def buscar_mayor(vec, actividad):
    mayor = None
    for cliente in vec:
        if cliente.actividad == actividad:
            if mayor is None or cliente.importe > mayor.importe:
                mayor = cliente
    return mayor


def buscar_id(vec, id):
    pos = -1
    for i in range(len(vec)):
        if vec[i].id == id:
            pos = i
            break
    return pos



def test():
    flags_vec = False
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            print('-'*45)
            print('Cargar vector:\n')
            n = validar_inf('Ingrese la cantidad de datos a cargar: ', 1)
            vec = generar_vec(n)
            print('-'*45)
            print('Vector cargado de forma exitosa!!!')
            print('-'*45)
            print('Datos del vector:\n')
            mostrar_vec(vec)
            flags_vec = True
        elif flags_vec:
            if op == 2:
                print('-'*45)
                print('Datos cuyo importe supere a un valor x:\n')
                importe = validar_inf('Ingrese importe mínimo: ', 0)
                print('-'*45)
                print('Datos con precio superior a: $', importe)
                mostrar_datos_importe(vec, importe)
            elif op == 3:
                print('-'*45)
                print('Importe total por actividad:\n')
                v_contador = generar_vc(vec, 19)
                mostrar_vc(v_contador)
            elif op == 4:
                print('-'*45)
                print('Cliente con mayor importe en actividad número 3:\n')
                mayor = buscar_mayor(vec, 3)
                print('-'*45)
                if mayor is None:
                    print('No se registraron clientes con actividad número 3....')
                else:
                    print('Datos del mayor:\n')
                    imprimir_cabecera()
                    campo.Cliente.to_strign(mayor)
            elif op == 5:
                print('-'*45)
                print('Buscar por id:\n')
                id = validar_rango('Ingrese ID a buscar: ', 1000, 9999)
                pos = buscar_id(vec, id)
                print('-'*45)
                if pos == -1:
                    print('El Id ingresado no existe...')
                else:
                    print('Id encontrado:\n')
                    imprimir_cabecera()
                    campo.Cliente.to_strign(vec[pos])


        else:
            print('-'*45)
            print('Es necesario primero generar el vector, ingrese primero a la opción número 1...')

        if op == 6:
            print('-'*45)
            print('Fin...')
test()
