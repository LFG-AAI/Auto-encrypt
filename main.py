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

def decrypt_file(input_filename, output_filename, password):
    try:
        # Read encrypted file
        with open(input_filename, 'rb') as f:
            encrypted_data = f.read()

        # Extract salt, IV, and ciphertext
        salt = encrypted_data[:16]
        iv = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]

        # Derive key from password and salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32 + 16,  # 32 bytes for key, 16 bytes for IV
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key_and_iv = kdf.derive(password.encode())
        key = key_and_iv[:32]

        # Decrypt ciphertext using AES-CBC mode
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Remove padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

        # Write decrypted plaintext to file
        with open(output_filename, 'wb') as f:
            f.write(unpadded_data)

        print(Fore.GREEN + f"File {input_filename} berhasil didekripsi dan disimpan sebagai {output_filename}")

    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan saat mendekripsi file {input_filename}: {str(e)}")

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
                            
                            
 Jangan lupa untuk subscribe channel 
      - All About the Internet -
 Telegram : https://t.me/allabout_internet
 Youtube  : @youtube-AAI
                            
                            

Script untuk mengenkripsi dan mendekripsi file teks menggunakan AES-CBC.

Cara penggunaan:
1. Jalankan skrip ini.
2. Masukkan nama file teks yang ingin Anda enkripsi atau dekripsi.
3. Masukkan nama file output untuk file hasil enkripsi atau dekripsi.
4. Masukkan password untuk enkripsi atau dekripsi.

Contoh penggunaan untuk enkripsi:
Masukkan nama file yang ingin dienkripsi: mytext.txt
Masukkan nama file output untuk file terenkripsi: mytext_encrypted.txt
Masukkan password untuk enkripsi: mypassword

Contoh penggunaan untuk dekripsi:
Masukkan nama file yang ingin didekripsi: mytext_encrypted.txt
Masukkan nama file output untuk file terdekripsi: mytext_decrypted.txt
Masukkan password untuk dekripsi: mypassword

File mytext.txt berhasil dienkripsi dan disimpan sebagai mytext_encrypted.txt.
File mytext_encrypted.txt berhasil didekripsi dan disimpan sebagai mytext_decrypted.txt.

===========================================================
""")

    mode = input("Pilih mode (enkripsi/e atau dekripsi/d): ").lower()

    if mode == 'enkripsi' or mode == 'e':
        input_filename = input("Masukkan nama file yang ingin dienkripsi: ")
        output_filename = input("Masukkan nama file output untuk file terenkripsi: ")
        password = input("Masukkan password untuk enkripsi: ")
        encrypt_file(input_filename, output_filename, password)

    elif mode == 'dekripsi' or mode == 'd':
        input_filename = input("Masukkan nama file yang ingin didekripsi: ")
        output_filename = input("Masukkan nama file output untuk file terdekripsi: ")
        password = input("Masukkan password untuk dekripsi: ")
        decrypt_file(input_filename, output_filename, password)

    else:
        print(Fore.RED + "Pilihan mode tidak valid. Silakan pilih 'enkripsi' atau 'dekripsi'.")
