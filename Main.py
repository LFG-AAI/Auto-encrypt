import py_compile
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

def encrypt_and_rename_file(input_filename, output_filename):
    try:
        # Kompilasi file Python menjadi bytecode
        compiled_filename = output_filename
        py_compile.compile(input_filename, cfile=compiled_filename)
        print(Fore.RED + f"File {input_filename} berhasil dienkripsi dan disimpan sebagai {compiled_filename}")

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
                            
                            
                            
                            
                            

Script untuk mengenkripsi file Python menjadi bytecode dan menamai output file sesuai input pengguna.

Cara penggunaan:
1. Jalankan skrip ini.
2. Masukkan nama file Python yang ingin Anda enkripsi (contoh.py).
3. Masukkan nama file output yang diinginkan tanpa ekstensi (contoh).
4. File bytecode akan disimpan dengan nama sesuai input pengguna.

Contoh penggunaan:
Masukkan nama file yang ingin dienkripsi (contoh.py): myscript.py
Masukkan nama file output yang diinginkan (contoh): myscript_encrypted

File myscript.py berhasil dienkripsi dan disimpan sebagai myscript_encrypted.

===========================================================
""")

    input_filename = input("Masukkan nama file yang ingin dienkripsi (contoh.py): ")
    output_filename = input("Masukkan nama file output yang diinginkan (contoh): ")

    encrypt_and_rename_file(input_filename, output_filename)
