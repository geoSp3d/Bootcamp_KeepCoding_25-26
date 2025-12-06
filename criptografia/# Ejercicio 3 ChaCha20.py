# Ejercicio 3 ChaCha20

from Crypto.Cipher import ChaCha20
import base64

# Key de KeyStore
CLAVE_HEX = "AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120"
clave_bytes = bytes.fromhex(CLAVE_HEX)

texto_original = "KeepCoding te enseña a codificar y a cifrar"
nonce_b64 = "9Yccn/f5nJJhAt2S"

# Decodificar el nonce (está en Base64)
nonce_bytes = base64.b64decode(nonce_b64)
print(f"Nonce decodificado: {nonce_bytes.hex()}")
print(f"Longitud del nonce: {len(nonce_bytes)} bytes")

# Cifrar con ChaCha20
cipher = ChaCha20.new(key=clave_bytes, nonce=nonce_bytes)
texto_cifrado = cipher.encrypt(texto_original.encode('utf-8'))

# Resultados
print(f"\n=== RESULTADOS CIFRADO CHACHA20 ===")
print(f"Texto original: {texto_original}")
print(f"Texto cifrado (hex): {texto_cifrado.hex()}")
print(f"Texto cifrado (Base64): {base64.b64encode(texto_cifrado).decode()}")
print(f"Longitud texto cifrado: {len(texto_cifrado)} bytes")

# Descifrado para comprobar que funciona en ambas direcciones
cipher_decrypt = ChaCha20.new(key=clave_bytes, nonce=nonce_bytes)
texto_descifrado = cipher_decrypt.decrypt(texto_cifrado)
print(f"Texto descifrado: {texto_descifrado.decode('utf-8')}")