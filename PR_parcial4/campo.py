# Una empresa de venta de electrodomésticos mantiene información sobre los distintos aparatos que tiene a la venta.
# Por cada aparato se registran los datos siguientes: número de identificación (un entero), nombre (una cadena),
# precio, tipo de aparato (un número entero entre 0 y 49 incluidos, para indicar
# (por ejemplo): 0: lavarropas, 1: televisor, etc.) y código de pais de origen
# (un valor entre 0 y 19, para indicar (por ejemplo): 0: Brasil, 1: USA, 2: Argentina, etc.)
# Se pide definir un tipo registro Aparato con los campos que se indicaron,
# y un programa completo con menú de opciones para hacer lo siguiente:
#
# 1- Cargar los datos de n registros de tipo Aparato en un arreglo de registros (cargue n por teclado).
# Valide que el tipo y el pais de origen estén dentro de los valores descriptos.
# Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual,
# TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática). El arreglo
# debe crearse de forma que siempre quede ordenado de menor a mayor, según el precio, y para hacer esto
# debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta
# la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción
# ordenada pero con búsqueda secuencial.
#
# 2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea.
#
# 3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación sea igual
# a num (cargar num por teclado).  Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe,
# informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
#
# 4- Usando el arreglo creado en el punto 1, determine la cantidad de aparatos de cada posible tipo por cada
# posible pais de origen (o sea, 50 * 20 contadores en una matriz de conteo). Muestre sólo los resultados diferentes de 0.
#
# 5- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los registros
# cuyo precio sea menor al precio promedio de todos los artículos del arreglo, y que además no sean del tipo 0.
#
# 6- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla.


class Aparato:
    def __init__(self, id, nombre, precio, aparato, pais):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.aparato = aparato
        self.pais = pais

    def to_string(self):
        cadena = '{:^4} | {:^15} | {:^8} | {:^7} | {:^4}'.format(self.id, self.nombre, self.precio, self.aparato, self.pais)
        print(cadena)
