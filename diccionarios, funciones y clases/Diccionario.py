# Declarar un diccionario en Python
student = {
    'name': 'Diego Alberto',
    'age': 25,
    'language': 'Python',
    'city': 'Lerna'
}

# Acceso a los valores de un diccionario
print(f'Contenido total del estudiante: {student}')
print(f'Nombre: {student["name"]}')
print(f'Edad: {student.get("age")}')
print('--- Operaciones básicas sobre diccionarios ---')

# Modificar los valores de un diccionario
student['language'] = 'C#'
print(f'\nContenido actual del estudiante una vez modificado el language: {student}')

# Eliminar un elemento de un diccionario
student.pop('city')
print(f'\nContenido del estudiante una vez eliminada la ciudad: {student}')

# Agregar un nuevo elemento
student['food'] = 'balletas'
print(f'Contenido del estudiante una vez agregada una nueva propiedad: {student}')

print("\n\n--- Iterar sobre un diccionario ---")
print("\nIteración de los elementos de un diccionario, simple")

for element in student:
    print(f"{element}: {student[element]}")

print("\nIteración de los elementos de un diccionario, destructuración - unpacking")

for key, value in student.items():
    print(f"Clave: {key}, Valor: {value}")

print("\nIteración de los elementos de un diccionario, claves")

for key in student.keys():
    print(f"Clave: {key}")

print("\nIteración de los elementos de un diccionario, valores")

for value in student.values():
    print(f"Valor: {value}")