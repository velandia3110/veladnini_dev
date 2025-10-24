import re

correos = ["juan@gmail.com", "andres@", "sofia123@hotmail.com", "test@"]
patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

for correo in correos:
    if re.match(patron, correo):
        print(f"Válido: {correo}")
    else:
        print(f"Inválido: {correo}")
