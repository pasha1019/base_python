import qrcode


qr_test = qrcode.QRCode(
    version=1,
    # управление исправлением ошибок
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # количество пикселей
    box_size=10,
    # толщина границы
    border=5,
)
qr_test.add_data("https://github.com/pasha1019")
qr_test.make(fit=True)
img_test = qr_test.make_image(fill_color='black', back_color='white')
img_test.save("some_file_qr.png")
