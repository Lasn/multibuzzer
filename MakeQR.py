import segno

qrcode = segno.make_qr("http://192.168.1.152:4000")
qrcode.save("QR_address.png", scale=20 )