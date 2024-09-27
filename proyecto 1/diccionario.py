# Define el diccionario de personas
personas = {"sofia": 19, "mario": 21, "elizabeth": 54, "lucas": 26}

# Abre el archivo de texto para escribir
with open("personas.txt", "w") as file:
    # Recorre el diccionario y escribe cada persona con el formato requerido
    for name, age in personas.items():
        formatted_name = name.capitalize()  # Capitaliza la primera letra del nombre
        file.write(f"{formatted_name}-{age}\n")  # Escribe la cadena formateada en el archivo
