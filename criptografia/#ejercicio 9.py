#ejercicio 9

import hashlib
from Crypto.Cipher import AES

# Clave AES-256 proporcionada
clave_hex = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
clave_bytes = bytes.fromhex(clave_hex)


print("\n CALCULO KCV - KEY CHECK VALUE")
print(f"Clave AES-256: {clave_hex}")
print(f"Longitud: {len(clave_bytes)} bytes = {len(clave_bytes)*8} bits\n")

# 1. KCV(SHA-256) - SHA-256 de la clave completa
print("1. KCV(SHA-256):")
sha256_hash = hashlib.sha256(clave_bytes).digest()  # bytes, no hexdigest
print(f"   SHA-256 completo: {sha256_hash.hex()}")
print(f"   Primeros 3 bytes: {sha256_hash[:3].hex()}")
print(f"   KCV(SHA-256): {sha256_hash[:3].hex().upper()}\n")

# 2. KCV(AES) - Cifrar 16 bytes de 0x00 con IV de 0x00
print("2. KCV(AES):")
# Bloque de 16 bytes de ceros (NO padding)
bloque_ceros = b'\x00' * 16  # Exactamente 16 bytes
iv_ceros = b'\x00' * 16

# Cifrar en CBC (sin padding - bloque exacto)
cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_ceros)
texto_cifrado = cipher.encrypt(bloque_ceros)

print(f"   Texto plano: {bloque_ceros.hex()}")
print(f"   IV: {iv_ceros.hex()}")
print(f"   Texto cifrado completo: {texto_cifrado.hex()}")
print(f"   Primeros 3 bytes: {texto_cifrado[:3].hex()}")
print(f"   KCV(AES): {texto_cifrado[:3].hex().upper()}")

print("\n" + "="*60)
print("RESULTADOS FINALES:")
print("="*60)
print(f"KCV(SHA-256): {sha256_hash[:3].hex().upper()}")
print(f"KCV(AES):     {texto_cifrado[:3].hex().upper()}")
print("="*60)