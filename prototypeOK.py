import hashlib

# Abrimos el archivo de salida "plain.txt"
with open("plain.txt", "w") as out_file:
    # Abrimos el archivo de hashes
    with open("hashes.txt", "r") as f:
        # Iteramos sobre cada línea del archivo
        for line in f:
            # Quitamos el carácter de nueva línea al final de la línea
            hash = line.strip()
            # Abrimos el archivo de contraseñas
            with open("passwords.txt", "r", encoding="latin-1") as p:
                password_found = False
                # Iteramos sobre cada contraseña del archivo
                for password in p:
                    # Quitamos el carácter de nueva línea al final de la contraseña
                    password = password.strip()
                    # Calculamos el hash de la contraseña
                    pwd_hash = hashlib.md5(password.encode()).hexdigest()
                    # Si el hash de la contraseña coincide con el hash del archivo, es la contraseña correcta
                    if pwd_hash == hash:
                        # Mostramos el resultado por pantalla
                        print(f"Hash crackeado: {hash} -> {password}")
                        # Escribimos el resultado en el archivo de salida
                        out_file.write(f"{password}\n")
                        password_found = True
                        break
                # Si no se encontró la contraseña, escribimos una línea en blanco en el archivo de salida
                if not password_found:
                    out_file.write("\n")
