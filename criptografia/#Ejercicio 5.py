#Ejercicio 5

import hashlib

# Textos
texto1 = "En KeepCoding aprendemos cómo protegernos con criptografía"
texto2 = "En KeepCoding aprendemos cómo protegernos con criptografía."  # Con punto

# Hashes dados
hash1_dado = "bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe"
hash2_dado = "4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833"

# 1. VERIFICAR HASH 1 (SHA3 Keccak)
print("\n1. Que tipo de SHA3 hemos generado?")
print(f"   Texto: '{texto1}'")

# Probar SHA3-256
sha3_256 = hashlib.sha3_256(texto1.encode()).hexdigest()
print(f"\n   SHA3-256 calculado: {sha3_256}")
print(f"   Hash proporcionado: {hash1_dado}")
print(f"   Coinciden? {sha3_256 == hash1_dado}")

if sha3_256 == hash1_dado:
    print("   RESPUESTA: SHA3-256 (Keccak de 256 bits)")

# 2. VERIFICAR HASH 2 (SHA2)
print("\n" + "-"*70)
print("\n2. Que hash SHA2 hemos realizado?")
print(f"   Longitud hash: {len(hash2_dado)} chars = {len(hash2_dado)//2} bytes = 512 bits")

# Probar SHA-512
sha512 = hashlib.sha512(texto1.encode()).hexdigest()
print(f"\n   SHA-512 calculado (primeros 32 chars): {sha512[:32]}...")
print(f"   Hash proporcionado (primeros 32 chars): {hash2_dado[:32]}...")
print(f"   Coinciden? {sha512 == hash2_dado}")

if sha512 == hash2_dado:
    print("   RESPUESTA: SHA-512 (SHA2 de 512 bits)")

# 3. GENERAR SHA3-256 DEL TEXTO CON PUNTO
print("\n" + "-"*70)
print("\n3. Generar SHA3-256 del texto con punto final")
print(f"   Texto original: '{texto1}'")
print(f"   Texto con punto: '{texto2}'")
print(f"   Diferencia: Un solo caracter (punto final)")

sha3_256_punto = hashlib.sha3_256(texto2.encode()).hexdigest()
print(f"\n   SHA3-256 sin punto: {sha3_256}")
print(f"   SHA3-256 con punto: {sha3_256_punto}")

# Calcular diferencia
print(f"\n   Comparacion caracter por caracter:")
coincidencias = sum(1 for a, b in zip(sha3_256, sha3_256_punto) if a == b)
porcentaje = (coincidencias / 64) * 100
print(f"   Caracteres iguales: {coincidencias}/64 ({porcentaje:.1f}%)")


print("1. SHA3-256 (Keccak de 256 bits)")
print("2. SHA-512 (SHA2 de 512 bits)")
