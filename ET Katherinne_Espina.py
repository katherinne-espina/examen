# ==========================================
# 1. DICCIONARIOS INICIALES (MUNDO PRINCIPAL)
# ==========================================

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

# ==========================================
# 2. FUNCIONES DE VALIDACIÓN GENERALES (OPCIÓN 4)
# ==========================================

def validar_no_vacio(texto):
    if not texto or texto.isspace():
        return False
    return True

def validar_codigo(codigo, dicc_libros):
    if not validar_no_vacio(codigo):
        return False
    # El código no debe existir ya (sin distinguir mayúsculas/minúsculas)
    for clave in dicc_libros.keys():
        if clave.upper() == codigo.upper():
            return False
    return True

def validar_anio(anio_str):
    try:
        anio = int(anio_str)
        return anio > 0
    except ValueError:
        return False

def validar_novedad(novedad_str):
    return novedad_str.lower() in ['s', 'n']

def validar_multa(multa_str):
    try:
        multa = int(multa_str)
        return multa > 0
    except ValueError:
        return False

def validar_copias(copias_str):
    try:
        copias = int(copias_str)
        return copias >= 0
    except ValueError:
        return False


# ==========================================
# 3. FUNCIONES ESPECÍFICAS DEL SISTEMA
# ==========================================

def leer_opcion():
    while True:
        try:
            opcion_str = input("Ingrese opción: ")
            opcion = int(opcion_str)
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def copias_genero(genero, dicc_libros, dicc_prestamos):
    total_copias = 0
    # for porque conocemos el volumen exacto de elementos del diccionario
    for cod, datos in dicc_libros.items():
        if datos[2].lower() == genero.lower():
            if cod in dicc_prestamos:
                total_copias += dicc_prestamos[cod][1]
    print(f"El total de copias disponibles es: {total_copias}")

def busqueda_multa(multa_min, multa_max, dicc_libros, dicc_prestamos):
    resultados = []
    for cod, datos_prestamo in dicc_prestamos.items():
        multa = datos_