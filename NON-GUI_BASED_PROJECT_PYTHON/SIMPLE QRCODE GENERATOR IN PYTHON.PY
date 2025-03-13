import qrcode
import sys
# "import qrcode as qr" This is used for make qr(allias) for qrcode.

def title():
    print("-----QR Code Maker-----")

i=input("Enter URL: ")
code_name=input("Enter QR Name: ")

def qr_maker():
    QR=qrcode.make(f"{i}")
    QR.save(f"{code_name}.png")

def exit():
    input("Press Enter to exit...")
    sys.exit()

def save():
    print("The QR Code is saved in the application file.")
    exit()

def qr():
    title()
    qr_maker()
    save()

qr()