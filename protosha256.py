import hashlib
import os

# Abrimos el fichero con los resultados de los hashes crackeados
with open("plain.txt", "r") as f:
  # Leemos todas las líneas del fichero
  lines = f.readlines()

# Creamos una lista para almacenar los nuevos hashes
new_hashes = []

# Iteramos sobre cada línea del fichero
for line in lines:
  # Quitamos el salto de línea al final de cada línea
  line = line.strip()

  # Si la línea no está vacía
  if line:
    # Generamos una sal aleatoria
    salt = os.urandom(16)

    # Calculamos el hash SHA256 con la sal
    hash = hashlib.sha256(salt + line.encode("utf-8")).hexdigest()

    # Mostramos el nuevo hash en pantalla
    print(hash)

    # Añadimos el nuevo hash a la lista
    new_hashes.append(hash)
  else:
    # Si la línea está vacía, añadimos una línea en blanco a la lista
    new_hashes.append("")

# Escribimos los nuevos hashes en un fichero
with open("new_passwords.txt", "w") as f:
  for hash in new_hashes:
    f.write(hash + "\n")
