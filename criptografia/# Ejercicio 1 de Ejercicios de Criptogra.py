# Ejercicio 1 de Ejercicios de Criptografia Finales

#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("B98A15BA31AEBB3F")

print(xor_data(m,k).hex())

num1=0xB1EF2ACFE2BAEEFF
num2=0xB98A15BA31AEBB3F
num3=(hex(num1^num2))
print(num3[2:])

