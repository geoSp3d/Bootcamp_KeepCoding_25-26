#Ejercicio13_Parte2.2

from cryptography.hazmat.primitives.asymmetric import ed25519
import nacl.signing
import hashlib

#Cargar

path_priv = r"C:\Users\d_gar\Desktop\GitHub Cripto\criptografia\Practica\ed25519-priv"
with open(path_priv, "rb") as f:
    private_bytes = f.read()

#private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_bytes)

# Solo los primeros 32 bytes
private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_bytes[:32])

#signedKey = ed25519.SigningKey(private_key)

#myhash = hashlib.sha256()
#myhash.update(bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.", "utf8"))
#msg_hasheado=myhash.digest()

# Crear hash SHA256 del mensaje
mensaje = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
hash_obj = hashlib.sha256(mensaje.encode('utf-8'))
msg_hasheado = hash_obj.digest()

#signature = signedKey.sign(msg_hasheado, encoding='hex')
signature = private_key.sign(msg_hasheado)


print("Firma Generada (64 bytes):", signature.hex())
