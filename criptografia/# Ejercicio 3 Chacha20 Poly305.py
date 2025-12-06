# Ejercicio 3 Chacha20 Poly305

from Crypto.Cipher import ChaCha20_Poly1305
import base64

# Key de KeyStore
CLAVE_HEX = "AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120"
clave_bytes = bytes.fromhex(CLAVE_HEX)

texto_original = "KeepCoding te enseña a codificar y a cifrar"
nonce_b64 = "9Yccn/f5nJJhAt2S"

# Nonce
nonce_bytes = base64.b64decode(nonce_b64)
print(f"Nonce: {nonce_b64} -> {nonce_bytes.hex()} ({len(nonce_bytes)} bytes)")

# En esta parte cifra y autentica
cipher = ChaCha20_Poly1305.new(key=clave_bytes, nonce=nonce_bytes)
texto_cifrado, tag = cipher.encrypt_and_digest(texto_original.encode('utf-8'))

print(f"\n CIFRADO COMPLETADO:")
print(f"Texto cifrado (Base64): {base64.b64encode(texto_cifrado).decode()}")
print(f"Tag autenticación (hex): {tag.hex()}")
print(f"Nonce (Base64): {nonce_b64}")


# Descifrado
try:
    cipher_verif = ChaCha20_Poly1305.new(key=clave_bytes, nonce=nonce_bytes)
    texto_descifrado = cipher_verif.decrypt_and_verify(texto_cifrado, tag)
    print(f"\n\n Comprobacion desencriptado: {texto_descifrado.decode('utf-8')}")
except ValueError as e:
    print(f"Error desencriptado: {e}")

