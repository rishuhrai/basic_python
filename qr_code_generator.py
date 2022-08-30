from lib2to3.pgen2.pgen import generate_grammar
import qrcode
def gen_qrcode(text):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save("qrimg.png")

gen_qrcode("https://pixabay.com/images/search/nature/")