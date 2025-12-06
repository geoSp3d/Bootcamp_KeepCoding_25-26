#Ejercicio 13

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import os

#Cargamos la clave PRIVADA porque generamos una firma
my_path = os.path.abspath(os.getcwd())
#path_file_priv = my_path + "/claveprivada-RSA_desc_oaep.pem" # <- Tengo problema al cargar el archivo de la firma esta es la ruta que yo tengo "C:\Users\d_gar\Desktop\clave-rsa-oaep-priv.pem" o "C:\Users\d_gar\Desktop\GitHub Cripto\criptografia\Practica\clave-rsa-oaep-priv.pem"
path_file_priv = r"C:\Users\d_gar\Desktop\GitHub Cripto\criptografia\Practica\clave-rsa-oaep-priv.pem"
#keypriv = RSA.importKey(open(path_file_priv).read())

with open(path_file_priv, 'rb') as f:
    keypriv = RSA.import_key(f.read())


mensaje_bytes = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.","utf-8")
hash = SHA256.new(mensaje_bytes)

firmador=PKCS115_SigScheme(keypriv) ## Generamos un Signer 
firma = firmador.sign(hash)
print("Firma: ", firma.hex())
