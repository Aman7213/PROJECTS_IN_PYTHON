import qrcode
import sys

def exit():
    input("Press Enter To Exit...")
    sys.exit()

def get_url():
    return input("Enter URl: ")

def front():
    return input("Enter QRCode Color: ")

def back():
    return input("Enter Background Color: ")

def file_name():
    z = input("Enter The Name Of File: ")
    xy = (f"{z}.png")
    return xy

data = get_url()
foreground = front()
background = back()
name = file_name()

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

def code():
    x=qr.make_image(fill_color=foreground, back_color=background)
    x.save(name)
    exit()

code()