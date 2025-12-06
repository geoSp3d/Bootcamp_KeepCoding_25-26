# Ejercicio 14

from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512

# Datos usados
salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
master = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

aes_key = HKDF(master, 32, salt, SHA512, 1)

print("Clave final: ", aes_key.hex())
expected_hex = "e716754c67614c53bd9bab176022c952a08e56f07744d6c9edb8c934f52e448a"
aes_key_hex = aes_key.hex()
print("¿Coincide con CyberChef?", aes_key_hex == expected_hex)