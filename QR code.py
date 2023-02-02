import pyqrcode

text = "Fuck you"

code = pyqrcode.create(text)
code.svg("qr.svg", scale=6)
