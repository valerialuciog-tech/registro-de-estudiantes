# Registro de estudiantes usando un diccionario

estudiantes = {}

# Agregar datos
nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota: "))
estudiantes[nombre] = nota

# Mostrar datos
print("\nEstudiantes registrados:")
for nombre, nota in estudiantes.items():
    print(nombre, "-", nota)

# Buscar estudiante
buscar = input("\nIngrese un nombre para buscar: ")

if buscar in estudiantes:
    print("Nota:", estudiantes[buscar])
else:
    print("Estudiante no encontrado.")
