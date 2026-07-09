# =====================================================================
#             EVALUACIÓN FINAL TRANSVERSAL - PYTHON (FPY1101)
# =====================================================================

# ---------------------------------------------------------------------
# 1. COMPONENTE: FUNCIONES DE BÚSQUEDA Y CONTROL DE MENÚ
# ---------------------------------------------------------------------

def leer_opcion() -> int:
    """
    [Indicador 24]: Define una función para leer la opción del menú que valida 
    que sea un entero dentro del rango permitido, maneja excepciones ante 
    entradas no numéricas y retorna la opción validada.
    """
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida (ingrese un número entero)")


def buscar_codigo(codigo: str, prestamos: dict) -> bool:
    """
    [Indicador 18, 25]: Implementa la lógica de búsqueda sobre el diccionario.
    Retorna True si el código existe (independiente de mayúsculas/minúsculas) o False.
    """
    codigo_limpio = codigo.strip().upper()
    for clave in prestamos.keys():
        if clave.upper() == codigo_limpio:
            return True
    return False


# ---------------------------------------------------------------------
# 2. COMPONENTE: FUNCIONES OPERATIVAS DEL SISTEMA
# ---------------------------------------------------------------------

def copias_genero(genero: str, libros: dict, prestamos: dict):
    """
    [Indicador 26]: Función con responsabilidad única para calcular 
    e imprimir el total de copias por género.
    """
    genero_buscado = genero.strip().lower()
    total_copias = 0
    
    # [Indicador 10]: Usa 'for' ya que el volumen de iteraciones del diccionario se conoce.
    for codigo, datos in libros.items():
        if datos[2].strip().lower() == genero_buscado:
            if codigo in prestamos:
                total_copias += prestamos[codigo][1]
                
    print(f"El total de copias disponibles es: {total_copias}")


def busqueda_multa(multa_min: int, multa_max: int, libros: dict, prestamos: dict):
    """
    [Indicador 18, 26]: Lógica de consulta por rango de multas y copias disponibles.
    """
    resultados = []
    for codigo, datos_prestamo in prestamos.items():
        precio_multa = datos_prestamo[0]
        copias = datos_prestamo[1]
        
        if multa_min <= precio_multa <= multa_max and copias > 0:
            if codigo in libros:
                titulo = libros[codigo][0]
                resultados.append(f"{titulo}--{codigo}")
                
    if resultados:
        resultados.sort()
        print(f"Los libros encontrados son: {resultados}")
    else:
        print("No hay libros en ese rango de multa.")


def actualizar_multa(codigo: str, nueva_multa: int, prestamos: dict) -> bool:
    """
    [Indicador 20, 31]: La función de modificación utiliza el VALOR RETORNADO 
    por la función de búsqueda para decidir si actualiza el registro o retorna False.
    """
    existe = buscar_codigo(codigo, prestamos)  # Invocación directa obligatoria
    
    if existe:
        codigo_limpio = codigo.strip().upper()
        # Localiza la clave real exacta dentro del diccionario
        for clave in prestamos.keys():
            if clave.upper() == codigo_limpio:
                prestamos[clave][0] = nueva_multa
                return True
    return False


def eliminar_libro(codigo: str, libros: dict, prestamos: dict) -> bool:
    """
    [Indicador 21, 30]: La función de eliminación utiliza el VALOR RETORNADO 
    por la función de búsqueda para decidir si elimina el registro o retorna False.
    """
    existe = buscar_codigo(codigo, prestamos)  # Invocación directa obligatoria
    
    if existe:
        codigo_limpio = codigo.strip().upper()
        # Localiza la clave real para borrar en ambos diccionarios
        clave_a_eliminar = None
        for clave in prestamos.keys():
            if clave.upper() == codigo_limpio:
                clave_a_eliminar = clave
                break
        if clave_a_eliminar:
            del libros[clave_a_eliminar]
            del prestamos[clave_a_eliminar]
            return True
    return False


# ---------------------------------------------------------------------
# 3. COMPONENTE: FUNCIONES DE VALIDACIÓN DE RESPONSABILIDAD ÚNICA
# ---------------------------------------------------------------------
# [Indicador 27]: Cada una recibe el dato, aplica condición exacta y retorna True o False.
# NO muestran mensajes de error internos (se delega al programa principal).

def validar_codigo(codigo: str, prestamos: dict) -> bool:
    if not codigo or codigo.isspace():
        return False
    if buscar_codigo(codigo, prestamos):
        return False
    return True

def validar_titulo(titulo: str) -> bool:
    return bool(titulo and not titulo.isspace())

def validar_autor(autor: str) -> bool:
    return bool(autor and not autor.isspace())

def validar_genero(genero: str) -> bool:
    return bool(genero and not genero.isspace())

def validar_anio(anio: str) -> bool:
    try:
        valor = int(anio)
        return valor > 0
    except ValueError:
        return False

def validar_editorial(editorial: str) -> bool:
    return bool(editorial and not editorial.isspace())

def validar_es_novedad(es_novedad: str) -> bool:
    return es_novedad.strip().lower() in ['s', 'n']

def validar_precio_multa(precio_multa: str) -> bool:
    try:
        valor = int(precio_multa)
        return valor > 0
    except ValueError:
        return False

def validar_copias_disponibles(copias: str) -> bool:
    try:
        valor = int(copias)
        return valor >= 0
    except ValueError:
        return False


def agregar_libro(codigo: str, titulo: str, autor: str, genero: str, anio: int, 
                  editorial: str, es_novedad: bool, precio_multa: int, 
                  copias_disponibles: int, libros: dict, prestamos: dict) -> bool:
    """
    [Indicador 19]: Implementa la inserción de un nuevo registro en ambos diccionarios.
    """
    if buscar_codigo(codigo, prestamos):
        return False
    
    codigo_f = codigo.strip().upper()
    libros[codigo_f] = [titulo.strip(), autor.strip(), genero.strip(), anio, editorial.strip(), es_novedad]
    prestamos[codigo_f] = [precio_multa, copias_disponibles]
    return True


# ---------------------------------------------------------------------
# 4. COMPONENTE: PROGRAMA PRINCIPAL (MAIN)
# ---------------------------------------------------------------------

def main():
    # [Indicador 15]: Diccionarios iniciales compartidos como fuentes de datos.
    libros = {
        'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
        'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
        'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
        'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
        'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
        'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
    }
    
    prestamos = {
        'L001': [500, 4],
        'L002': [700, 0],
        'L003': [300, 10],
        'L004': [400, 2],
        'L005': [600, 1],
        'L006': [350, 6]
    }

    # [Indicador 11]: Ciclo while activo hasta que el usuario decida salir.
    ejecutando = True
    while ejecutando:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Copias por género")
        print("2. Búsqueda de libros por rango de multa")
        print("3. Actualizar multa de libro")
        print("4. Agregar libro")
        print("5. Eliminar libro")
        print("6. Salir")
        print("=====================================")
        
        # [Indicador 28]: Invocación de funciones desde el programa principal.
        opcion = leer_opcion()
        
        # --- OPCIÓN 1: COPIAS POR GÉNERO ---
        if opcion == 1:
            gen = input("Ingrese género a consultar: ")
            # [Indicador 29]: Pasa los diccionarios como argumentos (sin usar variables globales).
            copias_genero(gen, libros, prestamos)
            
        # --- OPCIÓN 2: BÚSQUEDA POR RANGO DE MULTA ---
        elif opcion == 2:
            while True:
                try:
                    # [Indicador 13, 14]: Manejo de excepciones con mensajes de error claros.
                    m_min = int(input("Ingrese multa mínima: "))
                    m_max = int(input("Ingrese multa máxima: "))
                    
                    if m_min >= 0 and m_max >= 0 and m_min <= m_max:
                        busqueda_multa(m_min, m_max, libros, prestamos)
                        break
                    else:
                        print("Las multas deben ser mayores a 0 y la mínima menor o igual a la máxima.")
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
        # --- OPCIÓN 3: ACTUALIZAR MULTA ---
        elif opcion == 3:
            continuar = 's'
            while continuar == 's':
                cod = input("Ingrese código del libro: ")
                while True:
                    try:
                        n_multa = int(input("Ingrese nueva multa: "))
                        if n_multa > 0:
                            break
                        print("La multa debe ser un número entero positivo.")
                    except ValueError:
                        print("Debe ingresar un valor entero.")
                
                # El main actúa exclusivamente según el booleano retornado por la función
                if actualizar_multa(cod, n_multa, prestamos):
                    print("Multa actualizada")
                else:
                    print("El código no existe")
                
                continuar = input("¿Desea actualizar otra multa (s/n)?: ").strip().lower()

        # --- OPCIÓN 4: AGREGAR LIBRO ---
        elif opcion == 4:
            c_cod = input("Ingrese código del libro: ")
            c_tit = input("Ingrese título: ")
            c_aut = input("Ingrese autor: ")
            c_gen = input("Ingrese género: ")
            c_ani = input("Ingrese año de publicación: ")
            c_edi = input("Ingrese editorial: ")
            c_nov = input("¿Es novedad? (s/n): ")
            c_mul = input("Ingrese precio de multa: ")
            c_cop = input("Ingrese copias disponibles: ")
            
            # [Indicador 9, 27]: Orquestación en el Main evaluando el retorno True/False de cada validación independiente.
            if not validar_codigo(c_cod, prestamos):
                print("Error: Código inválido o ya existente.")
            elif not validar_titulo(c_tit):
                print("Error: El título no puede estar vacío.")
            elif not validar_autor(c_aut):
                print("Error: El autor no puede estar vacío.")
            elif not validar_genero(c_gen):
                print("Error: El género no puede estar vacío.")
            elif not validar_anio(c_ani):
                print("Error: El año debe ser un entero mayor que cero.")
            elif not validar_editorial(c_edi):
                print("Error: La editorial no puede estar vacía.")
            elif not validar_es_novedad(c_nov):
                print("Error: Debe ingresar 's' o 'n' para novedad.")
            elif not validar_precio_multa(c_mul):
                print("Error: El precio de la multa debe ser un entero mayor que cero.")
            elif not validar_copias_disponibles(c_cop):
                print("Error: Las copias deben ser un entero mayor o igual a cero.")
            else:
                # Transformaciones finales explícitas post-validación exitosa
                booleano_novedad = True if c_nov.strip().lower() == 's' else False
                if agregar_libro(c_cod, c_tit, c_aut, c_gen, int(c_ani), c_edi, booleano_novedad, int(c_mul), int(c_cop), libros, prestamos):
                    print("Libro agregado")
                else:
                    print("El código ya existe")

        # --- OPCIÓN 5: ELIMINAR LIBRO ---
        elif opcion == 5:
            cod_eliminar = input("Ingrese el código del libro a eliminar: ")
            # El programa principal decide qué imprimir basándose exclusivamente en el valor booleano
            if eliminar_libro(cod_eliminar, libros, prestamos):
                print("Libro eliminado")
            else:
                print("El código no existe")

        # --- OPCIÓN 6: SALIR ---
        elif opcion == 6:
            print("Programa finalizado.")
            ejecutando = False


if __name__ == "__main__":
    main()