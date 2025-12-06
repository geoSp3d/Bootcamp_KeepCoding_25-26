# Ejercicio 10  
# Parte 1: Verificar firma PGP de Pedro

import gnupg

# 1. Configurar GPG
gpg = gnupg.GPG()

# 2. Importar clave pública de Pedro
clave_pedro_pub = """-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEYrhG/BYJKwYBBAHaRw8BAQdADXLwl3iCWWDNmKoBmZ+/rKdz+8ulKz4cK7Pj
PdZu8Fy0NVBlZHJvIFBlZHJpdG8gUGVkcm8gPHBlZHJvLnBlZHJpdG8ucGVkcm9A
ZW1wcmVzYS5jb20+iJkEExYKAEEWIQQb3mNeTq5uaN+tL3zXML4ZbkZhAQUCYrhG
/AIbAwUJA8JnAAULCQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAKCRDXML4ZbkZh
AYAfAP4xudXYKg3d59Doa3eswATu+r1dfqXk6xbPHd7rTD5bbwEAjar0HIi7Xi3M
0m7LMRGEx5CKcSZYbkCXYwaAyUWm5w+4OARiuEb8EgorBgEEAZdVAQUBAQdANwkF
l/zIRjpNCCwhe6c4NDaEcdmegYUrsahIf+/6MmsDAQgHiH4EGBYKACYWIQQb3mNe
Tq5uaN+tL3zXML4ZbkZhAQUCYrhG/AIbDAUJA8JnAAAKCRDXML4ZbkZhAVusAQD3
PRwejqYh8WLV1sWPlDKkaU+vnfUaRYkpesu7ZSklbAD9EnmAr+dVK2VOW9e3f8h0
5VxGZQQMnBylOKKilTQM7gw=
=O3za
-----END PGP PUBLIC KEY BLOCK-----"""

print("Importando clave pública de Pedro...")
resultado = gpg.import_keys(clave_pedro_pub)
print(f"Claves importadas: {resultado.count}")

# 3. Mensaje de Pedro (según enunciado)
mensaje_pedro = """Se debe ascender inmediatamente a Raúl. Es necesario mejorarle sus condiciones económicas un 20% para que se quede con nosotros."""

print(f"\nMensaje de Pedro:\n{mensaje_pedro}")

# 4. Suponiendo que tienes la firma en un archivo .sig
# Si no, necesitamos generar firma de prueba primero
print("\n⚠️  Necesito el archivo 'MensajeRespoDeRaulARRHH.txt.sig'")
print("   O la firma en hexadecimal/texto")

# PARA PRUEBA: Crear firma de prueba (simulando que Pedro firmó)
firma_prueba = gpg.sign(mensaje_pedro, keyid=resultado.fingerprints[0])
print(f"\nFirma de prueba generada:\n{firma_prueba}")

# 5. Verificar (con firma de prueba)
print("\nVerificando firma...")
verificado = gpg.verify(firma_prueba.data)

if verificado.valid:
    print(f"✅ FIRMA VÁLIDA de {verificado.username}")
else:
    print(f"❌ FIRMA NO VÁLIDA")

# Pausa para Parte 2
print("\n" + "="*60)
print("Listo para Parte 2...")