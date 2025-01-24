import segno

text = input()
# Generate QR code
qrcode = segno.make_qr(text)
qrcode.save("QR_address.png", scale=20)
