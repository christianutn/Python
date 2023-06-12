# Un gimnasio desea un programa para procesar los datos de las inscripciones que recepta. Para cada operación de
# inscripción se tienen los siguientes datos: el número de identificación de la inscripción, el apellido de la persona
# que va a entrenar, el importe a cobrar por la actividad a realizar y la actividad deportiva en la que se inscriba
# (un número entero entre 0 y 18, por ejemplo: 0: Entrenamiento Funcional, 1: Pilates, etc.). Se desea almacenar
# información referida a las n inscripciones que recepta el gimnasio en un arreglo de registros de tipo Inscripción
# (definir el tipo Inscripción y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:
#
# Cargar el arreglo pedido con los datos de las n inscripciones. Valide que el número identificador de la inscripción
# sea positivo, que el importe a cobrar en concepto de la actividad a realizar sea mayor a cero, y que el número de
# actividad a realizar sea mayor o igual a 0 y menor o igual que 18. Puede hacer la carga en forma manual,
# o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea.
# Pero al menos una debe programar.

# Mostrar todos los datos de las inscripciones cuyo importe a cobrar por la actividad a realizar sea superior a un
# valor x, siendo x un valor que se carga por teclado, en un listado ordenado de menor a mayor según los apellidos
# de las personas que van a entrenar.

# Determinar y mostrar el importe total cobrado por cada tipo posible de actividad a realizar. En total,
# 19 acumuladores usando un vector de acumulación. Mostrar solo los valores del vector que sean distintos de cero.

# Determinar y mostrar los datos de la inscripción que posee el mayor precio entre las que se registraron para la
# actividad deportiva número 3. Si existe más de un registro que posea el mayor precio entre los que son tipo 3, mostrar sólo uno.

# Determinar si existe una inscripción cuyo número identificador sea igual a c, siendo c un valor que se carga por
# teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que
# coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.

class Cliente:
    def __init__(self, id, apellido, importe, actividad):
        self.id = id
        self.apellido = apellido
        self.importe = importe
        self.actividad = actividad

    def to_strign(self):
        cadena = '{:^4} | {:^15} | {:^7} | {:^9}'.format(self.id, self.apellido, self.importe, self.actividad)
        print(cadena)



