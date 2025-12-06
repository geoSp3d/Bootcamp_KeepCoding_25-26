import subprocess
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def extraer_clave_con_test():
    """Usa el test que sabemos que funciona"""
    print("Ejecutando extractor probado...")
    
    # Código Java que SABEMOS funciona
    java_code = '''
import java.io.FileInputStream;
import java.security.KeyStore;
import javax.crypto.SecretKey;

public class TestExtract {
    public static void main(String[] args) throws Exception {
        // Ruta ABSOLUTA - MODIFICA ESTA LÍNEA
        String keystorePath = "C:\\\\Users\\\\d_gar\\\\Desktop\\\\KeyStore\\\\KeyStorePracticas";
        String keystorePass = "123456";
        String keyAlias = "cifrado-sim-aes-256";
        String keyPass = "123456";
        
        KeyStore ks = KeyStore.getInstance("JCEKS");
        ks.load(new FileInputStream(keystorePath), keystorePass.toCharArray());
        
        SecretKey key = (SecretKey) ks.getKey(keyAlias, keyPass.toCharArray());
        
        byte[] keyBytes = key.getEncoded();
        StringBuilder hex = new StringBuilder();
        for (byte b : keyBytes) {
            hex.append(String.format("%02x", b));
        }
        
        System.out.print(hex.toString());
    }
}
'''
    
    # Crear archivo
    with open('TestExtract.java', 'w', encoding='utf-8') as f:
        f.write(java_code)
    
    # Compilar
    compile_result = subprocess.run(['javac', 'TestExtract.java'], 
                                   capture_output=True, text=True, shell=True)
    
    if compile_result.returncode != 0:
        print(f"Error compilando: {compile_result.stderr[:200]}")
        # Limpiar y salir
        if os.path.exists('TestExtract.java'):
            os.remove('TestExtract.java')
        return None
    
    # Ejecutar
    run_result = subprocess.run(['java', 'TestExtract'], 
                               capture_output=True, text=True, shell=True)
    
    # Limpiar
    for f in ['TestExtract.java', 'TestExtract.class']:
        if os.path.exists(f):
            os.remove(f)
    
    if run_result.returncode == 0 and run_result.stdout.strip():
        clave = run_result.stdout.strip()
        print(f"Clave extraída: {clave[:16]}...{clave[-16:]}")
        return clave
    else:
        print(f"[!]Error ejecutando: {run_result.stderr[:200]}")
        return None

def descifrar_mensaje(clave_hex):
    """Descifra el mensaje"""
    try:
        clave_bytes = bytes.fromhex(clave_hex)
        
        cifrado_base64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4US t3aB/i50nvvJbBiG+le1ZhpR84oI="
        cifrado_base64 = cifrado_base64.replace(" ", "")
        
        iv = b'\x00' * 16
        texto_cifrado_bytes = base64.b64decode(cifrado_base64)
        
        cipher = AES.new(clave_bytes, AES.MODE_CBC, iv)
        mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size)
        
        texto_claro = mensaje_des_bytes.decode('utf-8')
        
        print(f"\n TEXTO DESCIFRADO:")
        print(f"   {texto_claro}")
        
        print(f"\n ANÁLISIS:")
        print(f"   Longitud: {len(texto_claro)} caracteres")
        print(f"   Bytes UTF-8: {len(texto_claro.encode('utf-8'))}")
        
        padding = 16 - (len(texto_claro.encode('utf-8')) % 16)
        if padding == 16:
            padding = 0
        print(f"Padding PKCS7: {padding} byte(s)")
        
        return texto_claro
        
    except Exception as e:
        print(f"[!]Error descifrando: {e}")
        return None

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("Sistema de descifrado importando de libreria KeyStore")
    print("=" * 50)
    
    #Extraer clave automáticamente
    print("\n1. EXTRAYENDO CLAVE DEL KEYSTORE...")
    clave_hex = extraer_clave_con_test()   
    # DESCIFRAR
    print(f"\n2. DESCIFRANDO CON CLAVE: {clave_hex[:16]}...")
    resultado = descifrar_mensaje(clave_hex)
    
    print("\n" + "=" * 50)
    if resultado:
        print("EJERCICIO 2 RESUELTO EXITOSAMENTE")
    else:
        print("[!]HUBO ERRORES EN LA RESOLUCIÓN")
    print("=" * 50)