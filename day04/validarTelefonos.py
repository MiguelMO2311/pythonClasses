def validar_formato_email(email):
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False

def validar_emails(emails):
    emails_validos = {}
    for nombre, info in emails.items():
        email = info["email"]
        activated = info["activated"]
        # Verificar el formato del email
        if validar_formato_email(email):
            if activated:
                emails_validos[nombre] = email
            else:
                print(f"El email de {nombre} no está activo.")
        else:
            print(f"El email {email} no tiene un formato correcto.")
    return emails_validos

# Diccionario de emails a validar
emails = {
    "joaquin": {
        "email": "starseeker_noether@outlook.com",
        "activated": True
    },
    "rosalinda": {
        "email": "example@gmail.com",
        "activated": False
    },
    "incorrecto": {
        "email": "incorrecto@correo",
        "activated": True
    },
}

# Validar los emails
emails_validos = validar_emails(emails)
print("Emails válidos:", emails_validos)
