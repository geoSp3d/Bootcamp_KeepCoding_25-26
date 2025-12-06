# Ejercicio 12 - AES/GCM

from Crypto.Cipher import AES
import base64

# Datos que vamos a usar
CLAVE_HEX = "E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74"
clave_bytes = bytes.fromhex(CLAVE_HEX)

nonce_b64 = "9Yccn/f5nJJhAt2S"
nonce_bytes = base64.b64decode(nonce_b64)

texto_original = "He descubierto el error y no volveré a hacerlo mal"

print("=== CIFRADO AES/GCM ===")
print(f"Key: {CLAVE_HEX}")
print(f"Nonce: {nonce_b64} -> {nonce_bytes.hex()} ({len(nonce_bytes)} bytes)")
print(f"Texto original: {texto_original}")

# Cifrado GCM
cipher = AES.new(clave_bytes, AES.MODE_GCM, nonce=nonce_bytes)
texto_cifrado, tag = cipher.encrypt_and_digest(texto_original.encode('utf-8'))

print(f"\n RESULTADOS:")
print(f"Texto cifrado (hex): {texto_cifrado.hex()}")
print(f"Texto cifrado (Base64): {base64.b64encode(texto_cifrado).decode()}")
print(f"Tag autenticación (hex): {tag.hex()}")

# Descifrado para verificar que funciona a la inversa
try:
    cipher_verif = AES.new(clave_bytes, AES.MODE_GCM, nonce=nonce_bytes)
    texto_descifrado = cipher_verif.decrypt_and_verify(texto_cifrado, tag)
    print(f"\n Descifrado funciona: {texto_descifrado.decode('utf-8')}")
except Exception as e:
    print(f"\n [!]Error: {e}")
