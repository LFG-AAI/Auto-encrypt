from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

def encrypt_file(input_filename, output_filename, password):
    try:
        # Generate salt
        salt = os.urandom(16)

        # Derive key and IV from password and salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32 + 16,  # 32 bytes for key, 16 bytes for IV
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key_and_iv = kdf.derive(password.encode())
        key = key_and_iv[:32]
        iv = key_and_iv[32:]

        # Read plaintext file
        with open(input_filename, 'rb') as f:
            plaintext = f.read()

        # Encrypt plaintext using AES-CBC mode
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        # Write encrypted ciphertext to file
        with open(output_filename, 'wb') as f:
            f.write(salt + iv + ciphertext)

        print(Fore.RED + f"File {input_filename} berhasil dienkripsi dan disimpan sebagai {output_filename}")

    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan saat mengenkripsi file {input_filename}: {str(e)}")

if __name__ == "__main__":
    print(Fore.YELLOW + """
===========================================================
  ______    ______   ______ 
 /      \  /      \ /      |
/$$$$$$  |/$$$$$$  |$$$$$$/ 
$$ |__$$ |$$ |__$$ |  $$ |  
$$    $$ |$$    $$ |  $$ |  
$$$$$$$$ |$$$$$$$$ |  $$ |  
$$ |  $$ |$$ |  $$ | _$$ |_ 
$$ |  $$ |$$ |  $$ |/ $$   |
$$/   $$/ $$/   $$/ $$$$$$/ 
                            
                            
                            
                            
                            

Script untuk mengenkripsi file teks menggunakan AES-CBC.

Cara penggunaan:
1. Jalankan skrip ini.
2. Masukkan nama file teks yang ingin Anda enkripsi.
3. Masukkan nama file output untuk file teks terenkripsi.
4. Masukkan password untuk enkripsi.

Contoh penggunaan:
Masukkan nama file yang ingin dienkripsi: mytext.txt
Masukkan nama file output untuk file terenkripsi: mytext_encrypted.txt
Masukkan password untuk enkripsi: mypassword

File mytext.txt berhasil dienkripsi dan disimpan sebagai mytext_encrypted.txt.

===========================================================
""")

    input_filename = input("Masukkan nama file yang ingin dienkripsi: ")
    output_filename = input("Masukkan nama file output untuk file terenkripsi: ")
    password = input("Masukkan password untuk enkripsi: ")

    encrypt_file(input_filename, output_filename, password)
