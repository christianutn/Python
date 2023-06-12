import random

def es_invalida(cuenta):
    es_invalida = False
    cant_arroba = 0
    anterior = ''
    for i in range(len(cuenta)):
        if cuenta[i] == '@':
            cant_arroba += 1

        if cuenta[i] == '.' and anterior == '.':
            es_invalida = True
        anterior = cuenta[i]

    if cuenta[0] == '@' or cuenta[-1] == '@' or cant_arroba != 1:
            es_invalida = True

    if cuenta[0] == '.' or cuenta[-1] == '.':
            es_invalida = True

    return es_invalida



print('Bienvenido: Generación estadística sobre COVID-19')
print('-'*60)
cuenta = input('Ingrese cuenta de usuario con formato nombre@dominio: ')
if cuenta == '':
    cuenta = ' '
cont_w = 1
se_acabaron_intentos = False
while es_invalida(cuenta) and cont_w < 3:

    print('-'*60)
    print('Error, cuenta ingresada de forma incorrecta. Vuelva a intentar...')
    cuenta = input('Ingrese cuenta de usuario con formato nombre@dominio: ')
    cont_w += 1
    if cuenta == '':
        cuenta = ' '
    es_invalida(cuenta)
    if cont_w == 3 and es_invalida(cuenta):
        print('Se acabaron los intentos...')
        se_acabaron_intentos = True

if not se_acabaron_intentos:
    print('Cuenta válida!!')
    print('-'*60)
    n = int(input('Ingrese cantidad de pacientes a procesar: '))
    while n <= 0:
        print('-'*60)
        print('Error, la cantidad de pacientes debe ser un número entero mayor a cero...')
        n = int(input('Ingrese cantidad de pacientes a procesar: '))
    cant_positivos = 0
    ac_edad_riesgo = 0
    cant_gp_riesgo = 0
    cant_pers_salud = 0
    ac_edad_positivos = 0
    men_edad_autoc = None
    cant_capital = 0
    cant_gcordoba = 0
    cant_norte = 0
    cant_sur = 0
    cant_viaj_ext = 0
    cant_cs_contacto = 0
    cant_cs = 0
    cant_auto = 0
    total_casos = n

    for i in range(n):
        edad = random.randint(1, 120) # edad de 1 a 120 años
        test = random.randint(1, 2) # 1: positivos - 2: negativos
        personal_salud = random.randint(1, 2) # 1: Si es personal de salud - 2: No es personal de salud
        contacto = random.randint(1, 2) # 1: si tuvo contacto con casos confirmados 2: no tuvo contacto
        region = random.randint(1, 4) # 1: Capital - 2: Gran Córdoba - 3: Norte - 4: Sur
        viajo_exterior = random.randint(1, 2) # 1: Si viajó al exterior - 2: No viajó al exterior

        if test == 1: # test positivo
            cant_positivos += 1
            ac_edad_positivos += edad

            if region == 1:
                cant_capital += 1
            elif region == 2:
                cant_gcordoba += 1
            elif region == 3:
                cant_norte += 1
            elif region == 4:
                cant_sur += 1

            if viajo_exterior == 1:
                cant_viaj_ext += 1

            if contacto == 2 and personal_salud == 2 and viajo_exterior == 2:
                if men_edad_autoc == None or edad < men_edad_autoc:
                    men_edad_autoc = edad
                cant_auto += 1

        else: #test = 2 - negativo
            if edad > 60:
                ac_edad_riesgo += edad
                cant_gp_riesgo += 1

        if personal_salud == 1:
            cant_pers_salud += 1

        if contacto == 1:
            cant_cs_contacto += 1




    porc_positvos_totalcasos = cant_positivos/total_casos*100
    porc_capital = cant_capital/total_casos*100
    porc_gcord = cant_gcordoba/total_casos*100
    porc_norte = cant_norte/total_casos*100
    porc_sur = cant_sur/total_casos*100
    porc_pers_salud = cant_pers_salud/total_casos*100


    print('-'*60)
    print('Elija la opción según información a saber:\n ')
    print('1. Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.')
    print('2. Edad promedio de los pacientes que pertenecen a grupo de riesgo (para pertenecer al grupo de riesgo el '
          'test debe ser negativo y tener más de 60 años).')
    print('3. Cantidad y porcentaje que el personal de salud representa sobre el total de casos.')
    print('4. Edad promedio entre los casos confirmados.')
    print('5. Menor edad entre los casos autóctonos.')
    print('6. Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.')
    print('7. Cantidad de casos confirmados con viaje al exterior.')
    print('8. Cantidad de casos sospechosos en contacto con casos confirmados.')
    print('9. Las regiones sin casos confirmados.')
    print('10.Porcentaje de casos positivos autóctonos sobre el total de positivos. ')


    op_menu = int(input('\nOpción (con cero termina): '))
    while op_menu < 0 or op_menu > 10:
        print('-'*60)
        print('Error, opción ingresada de forma incorrecta, recuerde debe ingresar un número entero '
              'comprendido entre 1 y 10, ó cero para terminar...')
        op_menu = int(input('Opción (con cero termina): '))

    while op_menu > 0 and op_menu <= 10:
        if op_menu == 1:
            if cant_positivos > 0:
                print('-'*60)
                print('Hay', cant_positivos, 'casos confirmados positivos.')
                print('Representa el %', round(porc_positvos_totalcasos, 2), ' sobre el total de casos.', sep='')
            else:
                print('-'*60)
                print('No se registraron casos positivos.')

        elif op_menu == 2:
            if cant_gp_riesgo > 0:
                prom_gr = ac_edad_riesgo/cant_gp_riesgo
                print('-'*60)
                print('EL promedio de edad de los pacientes en grupo de riesgo es de', round(prom_gr, 2), 'años.')
            else:
                print('-'*60)
                print('No se registraron pacientes en grupo de riesgo.')

        elif op_menu == 3:
            if cant_pers_salud > 0:
                print('-'*60)
                print('Se registró', cant_pers_salud, 'paciente/s que pertenece/n al personal de salud.')
                print('Representan el %', round(porc_pers_salud, 2), 'sobre el total de casos.')
            else:
                print('-'*60)
                print('No se registraron pacientes pertenecientes al personal de salud.')

        elif op_menu == 4:
            if cant_positivos > 0:
                prom_edad_cc = ac_edad_positivos/cant_positivos
                print('-'*60)
                print('El promedio de edad de los pacientes con test positivo es de ', round(prom_edad_cc, 2), 'años.')
            else:
                print('-'*60)
                print('No se registraron casos positivos.')

        elif op_menu == 5:
            if cant_auto > 1:
                print('-'*60)
                print('El paciente con menor edad entre los casos autóctonos tiene', men_edad_autoc, 'años.')
            elif cant_auto == 1:
                print('-'*60)
                print('Sólo se registró un paciente "caso autóctono" con una edad de', men_edad_autoc, 'años.')
            elif cant_auto == 0:
                print('-'*60)
                print('No se registraron pacientes "caso autóctono".')

        elif op_menu == 6:
            if cant_capital > 0:
                print('-'*60)
                print('En Córdoba Capital se registrò', cant_capital, 'caso/s confirmado/s.')
                print('Representan el %', porc_capital, ' con respecto al total de casos.', sep='')
            else:
                print('-'*60)
                print('No hubo casos confirmados en Córdoba Capital.')


            if cant_gcordoba > 0:
                print('-'*60)
                print('En Gran Córdoba se registrò', cant_gcordoba, 'caso/s confirmado/s.')
                print('Represantan el %', round(porc_gcord, 2), ' con respecto al total de casos.', sep='')
            else:
                print('-'*60)
                print('No hubo casos confirmados en Gran Córdoba.')

            if cant_norte > 0:
                print('-'*60)
                print('En Córdoba Norte se registrò', cant_norte, 'caso/s confirmado/s.')
                print('Represantan el %', round(porc_norte, 2), ' con respecto al total de casos.', sep='')
            else:
                print('-'*60)
                print('No hubo casos confirmados en Córdoba Norte')

            if cant_sur > 0:
                print('-'*60)
                print('En Córdoba Sur se registrò', cant_sur, 'caso/s confirmado/s.')
                print('Represantan el %', round(porc_sur, 2), ' con respecto al total de casos.', sep='')
            else:
                print('-'*60)
                print('No hubo casos confirmados en Córdoba Sur.')

        elif op_menu == 7:
            if cant_viaj_ext > 0:
                print('-'*60)
                print('Se registró', cant_viaj_ext, 'caso/s confirmado/s que viajaron al exterior.')
            else:
                print('-'*60)
                print('No se registraron casos positivos que además hayan viajado al exterior.')

        elif op_menu == 8:
            if cant_cs_contacto > 0:
                print('-'*60)
                print('Se registró', cant_cs_contacto, ' paciente/s "caso sopechoso" que tuvieron contacto con casos positivos.')
            else:
                print('-'*60)
                print('No se registró pacientes que tuvieran contacto con casos confirmados.')

        elif op_menu == 9:
            print('-'*60)
            print('Las regiones sin casos confirmados fueron:\n ')
            i = 1
            if cant_capital == 0:
                print(str(i), '. Córdoba Capital.', sep='')
                i += 1
            if cant_gcordoba == 0:
                print(str(i), '. Gran Córdoba.', sep='')
                i += 1
            if cant_norte == 0:
                print(str(i), '. Córdoba Norte.', sep='')
                i += 1
            if cant_sur == 0:
                print(str(i), '. Córdoba Sur.', sep='')
                i += 1
            if i == 1:
                print('No se registraron zonas sin casos confirmados.')

        elif op_menu == 10:
            if cant_auto > 0:
                porc_ca_positivos = cant_auto/cant_positivos*100
                print('-'*60)
                print('Los casos autòctonos representan el %', round(porc_ca_positivos, 2), sep='')
            else:
                print('-'*60)
                print('No se presentaron casos autóctonos')
        print('-'*60)
        op_menu = int(input('Opción (con cero termina): '))
        while op_menu < 0 or op_menu > 10:
            print('-'*60)
            print('Error, opción ingresada de forma incorrecta, recuerde debe ingresar un número entero '
                  'comprendido entre 1 y 10, ó cero para terminar...')
            op_menu = int(input('Opción (con cero termina): '))
    if op_menu == 0:
        print('Fin...')

else:
    print('Debe volver a ejecutar programa desde cero...')
