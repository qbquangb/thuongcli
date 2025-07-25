import argparse
import os
from thuonglib.encrypt_decrypt_file import encrypt_file as encrypt_file_XOR, decrypt_file as decrypt_file_XOR
from thuonglib.c_by_hand import control_by_hand
from thuonglib.delete_folder import clean_files_temp, del_dir_downloads
from thuonglib.password_cipher import p_cipher
from thuonglib.divide_merge_file import divide_file, merge_file
from thuonglib.AES_CBC import encrypt_file_AES_CBC, decrypt_file_AES_CBC
from thuonglib.RSA_OAEP import export_keys_RSA_OAEP, encrypt_file as encrypt_file_rsa, decrypt_file as decrypt_file_rsa
from thuonglib.AES_CTR import encrypt_file_AES_CTR, decrypt_file_AES_CTR
from thuonglib.AES_GCM import encrypt_file_AES_GCM, decrypt_file_AES_GCM
from thuonglib.HASH import sha256

def main():
    parser = argparse.ArgumentParser(
        prog="cli",
        usage="mo CMD va nhan cli --help",
        description="Chuong trinh dieu khien may tinh bang dong lenh.\n"
                    "Chuong trinh duoc viet boi Tran Dinh Thuong.\n"
                    "Email: qbquangbinh@gmail.com"
    )
    parser.add_argument("--name", "-n", help="Your name", default="Tran Dinh Thuong")
    parser.add_argument("--shutdown", "-s", action="store_true", help="Shutdown the computer")
    parser.add_argument("--restart", "-r", action="store_true", help="Restart the computer")
    parser.add_argument("--sleep", "-sl", action="store_true", help="Put the computer to sleep")
    parser.add_argument("--version", "-v", action="version", version="mycli 1.0.9", help="Show version information")
    parser.add_argument("--youtube", "-y", action="store_true", help="Open YouTube in the default web browser")
    parser.add_argument("--clean", "-c", action="store_true", help="Clean temporary files")
    parser.add_argument("--deepclean", "-dc", action="store_true", help="Xoa tat ca các tep va thu muc trong thu muc Downloads")
    parser.add_argument("--control_hand", "-ch", action="store_true", help="Dieu khien may tinh bang cu chi tay.")
    parser.add_argument("--div_mer_file", "-dmf", action="store_true", help="Chia va ghep file.")
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = False

    cipher_text_parser = subparsers.add_parser("cipher", help="Ma hoa van ban bang XOR cipher.")

    XOR_file_parser = subparsers.add_parser("XOR", help="Mã hóa file và giải mã file bằng XOR cipher.")
    XOR_file_parser.add_argument("--encrypt_file", "-ef", action="store_true", help="Mã hóa file bằng XOR cipher.")
    XOR_file_parser.add_argument("--decrypt_file", "-df", action="store_true", help="Giải mã file bằng XOR cipher.")

    AES_CBC_parser = subparsers.add_parser("AES_CBC", help="Chương trình mã hóa và giải mã file bằng AES-CBC.")
    AES_CBC_parser.add_argument("--encrypt_file", "-ef", action="store_true", help="Mã hóa file bằng AES-CBC.")
    AES_CBC_parser.add_argument("--decrypt_file", "-df", action="store_true", help="Giải mã file bằng AES-CBC.")
    # ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤
    AES_CTR_parser = subparsers.add_parser("AES_CTR", help="Chương trình mã hóa và giải mã file bằng AES-CTR.")
    AES_CTR_parser.add_argument("--encrypt_file", "-ef", action="store_true", help="Mã hóa file bằng AES-CTR.")
    AES_CTR_parser.add_argument("--decrypt_file", "-df", action="store_true", help="Giải mã file bằng AES-CTR.")
    # ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤
    AES_GCM_parser = subparsers.add_parser("AES_GCM", help="Chương trình mã hóa và giải mã file bằng AES-GCM.")
    AES_GCM_parser.add_argument("--encrypt_file", "-ef", action="store_true", help="Mã hóa file bằng AES-GCM.")
    AES_GCM_parser.add_argument("--decrypt_file", "-df", action="store_true", help="Giải mã file bằng AES-GCM.")
    # ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤
    AES_RSA_parser = subparsers.add_parser("AES_RSA", help="Chương trình tạo khóa RSA, mã hóa và giải mã file bằng AES-CBC và RSA-OAEP.")
    AES_RSA_parser.add_argument("--generate_keys", "-gk", action="store_true", help="Tạo cặp khóa RSA (public và private).")
    AES_RSA_parser.add_argument("--encrypt_file", "-ef", action="store_true", help="Mã hóa file bằng AES-CBC và khóa RSA.")
    AES_RSA_parser.add_argument("--decrypt_file", "-df", action="store_true", help="Giải mã file bằng AES-CBC và khóa RSA.")
    # ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤
    hash_parser = subparsers.add_parser("hash", help="Tạo giá trị băm SHA256, SHA512, SHA3_256, SHA3_512 từ dữ liệu đầu vào.")
    hash_parser.add_argument("--algorithm", "-a", choices=["SHA256", "SHA512", "SHA3_256", "SHA3_512"], default="SHA256", 
                             help="Chọn thuật toán băm SHA256, SHA512, SHA3_256, SHA3_512 (mặc định là SHA256).")
    hash_parser.add_argument("data", type=str, 
                             help="Dữ liệu đầu vào để băm, chuỗi data hoặc chuỗi rỗng nếu tạo giá trị hash bằng với file.")
    
    args = parser.parse_args()
    print(f"Hello, {args.name}!")
    if args.shutdown:
        os.system("shutdown /s /t 0")
    elif args.restart:
        os.system("shutdown /r /t 0")
    elif args.sleep:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 1,1,1")
    elif args.youtube:
        os.system("start https://www.youtube.com")
    elif args.clean:
        clean_files_temp()
            
    elif args.deepclean:
        del_dir_downloads()
        
    elif args.control_hand:
        control_by_hand()
    elif args.command == "cipher":
        p_cipher()
    elif args.command == "XOR":
        if args.encrypt_file:
            encrypt_file_XOR()
        elif args.decrypt_file:
            decrypt_file_XOR()
    elif args.div_mer_file:
        print("Chia va ghep file.")
        choice = input("Nhap lua chon cua ban (d/m): ").lower()
        while choice not in ['d', 'm']:
            choice = input("Nhap 'd' de chia file, 'm' de ghep file: ").lower()
        if choice == 'd':
            divide_file()
        else:
            merge_file()
    elif args.command == "AES_CBC":
        if args.encrypt_file:
            encrypt_file_AES_CBC()
        elif args.decrypt_file:
            decrypt_file_AES_CBC()
    elif args.command == "AES_RSA":
        if args.generate_keys:
            export_keys_RSA_OAEP()
        elif args.encrypt_file:
            encrypt_file_rsa()
        elif args.decrypt_file:
            decrypt_file_rsa()
    elif args.command == "AES_CTR":
        if args.encrypt_file:
            encrypt_file_AES_CTR()
        elif args.decrypt_file:
            decrypt_file_AES_CTR()
    elif args.command == "AES_GCM":
        if args.encrypt_file:
            encrypt_file_AES_GCM()
        elif args.decrypt_file:
            decrypt_file_AES_GCM()
    elif args.command == "hash":
        if args.algorithm == "SHA256":
            sha256(args.data, file_write=0 if args.data else 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()