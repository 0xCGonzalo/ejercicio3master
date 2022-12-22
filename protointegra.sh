#!/bin/bash
echo ""
echo "Ejecutando crackeo de contraseñas..."
echo ""
python prototypeOK.py
echo ""
sleep(8)
echo "Ejecutando cifrado en SHA256 de contraseñas en texto plano..."
echo ""
python protosha256.py
echo ""
echo "Proceso finalizado. Resultados guardados en fichero 'new_passwords.txt'"
