import pyqrcode

def qrcode():
    print("Write a Text to generate a QR code")
    q = pyqrcode.create(input())
    q.png('qrcode.png',scale=6)
    print("QR code generated")

if __name__ == '__main__' :
    qrcode()
