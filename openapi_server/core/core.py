import io
import json
import base64
import qrcode
import logging
import urllib.parse
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *


logger = logging.getLogger(__name__)


def image_to_byte_array(image:Image, imgFormat):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=imgFormat)
    return imgByteArr.getvalue()


frames = {
    "default": SquareModuleDrawer(),
    "square": SquareModuleDrawer(),
    "gapped-square": GappedSquareModuleDrawer(),
    "circle": CircleModuleDrawer(),
    "rounded": RoundedModuleDrawer(),
    "vertical-bars": VerticalBarsDrawer(),
    "horizontal-bars": HorizontalBarsDrawer()
}

masks = {
    "default": SolidFillColorMask(),
    "solid-fill": SolidFillColorMask(),
    "radial-gradiant": RadialGradiantColorMask(),
    "square-gradiant": SquareGradiantColorMask(),
    "horizontal-gradiant": HorizontalGradiantColorMask(),
    "vertical-gradiant": VerticalGradiantColorMask()
}

def email_qrcode(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  box_size=10,
    border=4, version=1)
    mail = "mailto:{}?SUB:{}&BODY:{}".format(
        urllib.parse.quote_plus(data['email']), 
        urllib.parse.quote_plus(data['objet']), 
        urllib.parse.quote_plus(data['payload']))
    qr.add_data(mail)
    if data['frame']:
        frm = data['frame']
    else:
        frm = "default"
    if data['shape']:
        msk = data['shape']
    else:
        msk = "default"
    if data['logo']:
        img = data['logo']
    else:
        img = None
    qr.make(fit=True)
    res = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=frames[frm], 
            color_mask=masks[msk],
            embeded_image_path=img, 
            fill_color= data['fill_color'] if ('fill_color' in data) else "black", 
            back_color= data['back_color'] if ('back_color' in data) else "white")
    qr.clear()
    return image_to_byte_array(res, 'PNG')


def sms_qrcode(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  box_size=10,
    border=4, version=1)
    sms = "SMSTO:{}:{}".format(
        data['numero'], data['payload'])
    qr.add_data(sms)
    if data['frame']:
        frm = data['frame']
    else:
        frm = "default"
    if data['shape']:
        msk = data['shape']
    else:
        msk = "default"
    if data['logo']:
        img = data['logo']
    else:
        img = None
    qr.make(fit=True)
    res = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=frames[frm], 
            color_mask=masks[msk],
            embeded_image_path=img, 
            fill_color= data['fill_color'] if ('fill_color' in data) else "black", 
            back_color= data['back_color'] if ('back_color' in data) else "white")
    qr.clear()
    return image_to_byte_array(res, 'PNG')


def text_qrcode(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  box_size=10,
    border=4, version=1)
    qr.add_data(data['payload'])
    if data['frame']:
        frm = data['frame']
    else:
        frm = "default"
    if data['shape']:
        msk = data['shape']
    else:
        msk = "default"
    if data['logo']:
        img = data['logo']
    else:
        img = None
    qr.make(fit=True)
    res = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=frames[frm], 
            color_mask=masks[msk],
            embeded_image_path=img, 
            fill_color= data['fill_color'] if ('fill_color' in data) else "black", 
            back_color= data['back_color'] if ('back_color' in data) else "white")
    qr.clear()
    return image_to_byte_array(res, 'PNG')
    


def url_qrcode(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  box_size=10,
    border=4, version=1)
    qr.add_data(data['payload'])
    if data['frame']:
        frm = data['frame']
    else:
        frm = "default"
    if data['shape']:
        msk = data['shape']
    else:
        msk = "default"
    if data['logo']:
        img = data['logo']
    else:
        img = None
    qr.make(fit=True)
    res = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=frames[frm], 
            color_mask=masks[msk],
            embeded_image_path=img, 
            fill_color= data['fill_color'] if ('fill_color' in data) else "black", 
            back_color= data['back_color'] if ('back_color' in data) else "white")
    qr.clear()
    return image_to_byte_array(res, 'PNG')


def vcard_qrcode(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  box_size=10,
    border=4, version=1)
    vcard = """BEGIN:VCARD
                N: {}; {};
                TEL;TYPE=work,VOICE: {}
                TEL;TYPE=home,VOICE: {}
                TEL;TYPE=fax: {}
                EMAIL: {}
                ORG: {}
                TITLE: {}
                ADR;TYPE=WORK,PREF:;;{};{};{};{};{}
                URL: {}
                VERSION:3.0
                END:VCARD
            """.format(
        data['name'], 
        data['surname'], 
        data['work_tel'], 
        data['home_tel'], 
        data['fax_tel'], 
        data['email'], 
        data['organisation'], 
        data['title'],
        data['road'],
        data['town'],
        data['town_code'], 
        data['zipcode'], 
        data['country'], 
        data['url']
    )
    qr.add_data(vcard)
    if data['frame']:
        frm = data['frame']
    else:
        frm = "default"
    if data['shape']:
        msk = data['shape']
    else:
        msk = "default"
    if data['logo']:
        img = data['logo']
    else:
        img = None
    qr.make(fit=True)
    res = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=frames[frm], 
            color_mask=masks[msk],
            embeded_image_path=img, 
            fill_color= data['fill_color'] if ('fill_color' in data) else "black", 
            back_color= data['back_color'] if ('back_color' in data) else "white")
    qr.clear()
    return image_to_byte_array(res, 'PNG')


def wifi_qrcode(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  box_size=10,
    border=4, version=1)
    wifi = "WIFI:T:{};S:{};P:{};H:{};;".format(
        data['cryptage'], data['network'],data['password'] ,data['hiddenNetwork'])
    qr.add_data(wifi)
    if data['frame']:
        frm = data['frame']
    else:
        frm = "default"
    if data['shape']:
        msk = data['shape']
    else:
        msk = "default"
    if data['logo']:
        img = data['logo']
    else:
        img = None
    qr.make(fit=True)
    logger.info(data)
    res = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=frames[frm], 
            color_mask=masks[msk],
            embeded_image_path=img, 
            fill_color= data['fill_color'] if ('fill_color' in data) else "black", 
            back_color= data['back_color'] if ('back_color' in data) else "white")
    qr.clear()
    return image_to_byte_array(res, 'PNG')


def get_health():
    return {"status": "ok"}