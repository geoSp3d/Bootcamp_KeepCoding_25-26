# Ejercicio 13 - Parte 2

from cryptography.hazmat.primitives.asymmetric import ed25519

# Cargar clave privada 

path_priv = r"C:\Users\d_gar\Desktop\GitHub Cripto\criptografia\Practica\ed25519-priv"
with open(path_priv, "rb") as f:
    private_bytes = f.read()

# Verificar si ha cargado bien [!] Aqui siempre tenemos problemas! <- Revisamos también tamaño correcto
print(f"Clave leída: {len(private_bytes)} bytes")

#private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_bytes)

# Tomar solo los primeros 32 bytes
clave_priv_32_bytes = private_bytes[:32]

private_key = ed25519.Ed25519PrivateKey.from_private_bytes(clave_priv_32_bytes)

# Mensaje
mensaje = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
firma = private_key.sign(mensaje.encode('utf-8'))

print("Firma Ed25519:", firma.hex())