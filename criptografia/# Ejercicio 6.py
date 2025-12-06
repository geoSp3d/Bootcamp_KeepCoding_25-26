# Ejercicio 6

from Crypto.Hash import HMAC, SHA256


clave_bytes = bytes.fromhex("A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB")

datos = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "utf8")

hmac256 = HMAC.new(clave_bytes, msg=datos, digestmod=SHA256)
print(hmac256.hexdigest())

# Resultado esperado : 857d5ab916789620f35bcfe6a1a5f4ce98200180cc8549e6ec83f408e8ca0550

# Comparativa resultado facilitado con el mio
resultado = hmac256.hexdigest()
esperado = "857d5ab916789620f35bcfe6a1a5f4ce98200180cc8549e6ec83f408e8ca0550"
print(f"{'Ok' if resultado == esperado else '[!]'} {resultado}")