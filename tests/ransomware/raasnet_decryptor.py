import os, sys
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pymsgbox import *
from Crypto import Random
from Crypto.Cipher import AES


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def decrypt(ciphertext, key):
    iv = ciphertext[: AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size :])
    return plaintext.rstrip(b"\0")


def decrypt_file(file_name, key):
    with open(file_name, "rb") as f:
        ciphertext = f.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-6], "wb") as f:
        f.write(dec)


def dec_key():
    key = password(text="Please enter your decryption key", title="Enter Key", mask="*")
    if key == None or key == "":
        messagebox.showwarning("Error", "No key given. Canceled...")
        sys.exit(1)
    return key


def dec_path():
    path = askdirectory(title="Select directory with files to decrypt")
    if path == None or path == "":
        messagebox.showwarning("Error", "No path selected, exiting...")
        sys.exit(1)
    path = path + "/"
    return path


def decrypt_files():
    key = dec_key()
    key = key.encode("utf-8")
    p = dec_path()

    a = messagebox.askokcancel(
        "WARNING",
        "This tool will decrypt your files with the given key.\n\nHowever, if your key or method is not correct, your (encrypted) files will return corrupted.\n\n You might want to make a backup!",
    )
    if a == True:
        pass
    else:
        return

    try:
        counter = 0
        for path, subdirs, files in os.walk(p):
            for name in files:
                try:
                    if name.endswith(".DEMON"):
                        decrypt_file(os.path.join(path, name), key)
                        os.remove(os.path.join(path, name))
                        print("[Decrypted] %s" % name)
                        counter += 1
                    elif name == "README.txt":
                        os.remove(os.path.join(path, name))
                        print("[DELETED] %s/%s" % (path, name))
                    else:
                        print("[Skipped] %s" % name)
                except Exception as e:
                    print("[ERROR] %s" % e)
                    pass

        print("\n[DONE] Decrypted %i files" % counter)

    except KeyboardInterrupt:
        print("\nInterrupted!\n")
        sys.exit(0)
    except Exception as e:
        print("\n[ ERROR ] %s" % e)
        sys.exit(1)


Tk = Tk()
Tk.withdraw()

decrypt_files()
