import connexion
import six

from openapi_server.models.email_schema import EmailSchema  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.sms_schema import SmsSchema  # noqa: E501
from openapi_server.models.src_schema import SrcSchema  # noqa: E501
from openapi_server.models.text_schema import TextSchema  # noqa: E501
from openapi_server.models.url_schema import UrlSchema  # noqa: E501
from openapi_server.models.vcard_schema import VcardSchema  # noqa: E501
from openapi_server.models.wifi_schema import WifiSchema  # noqa: E501
from openapi_server import util

from openapi_server.core.core import *


def api_v1_qrcode_email_post(email_schema=None):  # noqa: E501
    """returns a qrcode that contains email data

     # noqa: E501

    :param email_schema: email in the qrcode
    :type email_schema: dict | bytes

    :rtype: SrcSchema
    """
    if connexion.request.is_json:
        email_schema = EmailSchema.from_dict(connexion.request.get_json())  # noqa: E501
        email_schema = {
            "email": email_schema.email,
            "objet": email_schema.objet,
            "payload": email_schema.payload,
            "frame": email_schema.frame,
            "shape": email_schema.shape,
            "logo": email_schema.logo
        }
    return email_qrcode(email_schema)


def api_v1_qrcode_sms_post(sms_schema=None):  # noqa: E501
    """returns a qrcode that contains sms credentials

     # noqa: E501

    :param sms_schema: phone number and payload of the qrcode
    :type sms_schema: dict | bytes

    :rtype: SrcSchema
    """
    if connexion.request.is_json:
        sms_schema = SmsSchema.from_dict(connexion.request.get_json())  # noqa: E501
        sms_schema = {
            "numero": sms_schema.numero,
            "payload": sms_schema.payload,
            "frame": sms_schema.frame,
            "shape": sms_schema.shape,
            "logo": sms_schema.logo
        }
    return sms_qrcode(sms_schema)


def api_v1_qrcode_text_post(text_schema=None):  # noqa: E501
    """returns a qrcode that contains simple text (500 characters maximum)

     # noqa: E501

    :param text_schema: title and payload of the qrcode
    :type text_schema: dict | bytes

    :rtype: SrcSchema
    """
    if connexion.request.is_json:
        text_schema = TextSchema.from_dict(connexion.request.get_json())  # noqa: E501
        text_schema = {
            "payload": text_schema.payload,
            "frame": text_schema.frame,
            "shape": text_schema.shape,
            "logo": text_schema.logo
        }
    return text_qrcode(text_schema)


def api_v1_qrcode_url_post(url_schema=None):  # noqa: E501
    """returns a qrcode that contains url data

     # noqa: E501

    :param url_schema: url in the qrcode
    :type url_schema: dict | bytes

    :rtype: SrcSchema
    """
    if connexion.request.is_json:
        url_schema = UrlSchema.from_dict(connexion.request.get_json())  # noqa: E501
        url_schema = {
            "payload": url_schema.payload,
            "frame": url_schema.frame,
            "shape": url_schema.shape,
            "logo": url_schema.logo
        }
    return url_qrcode(url_schema)


def api_v1_qrcode_vcard_post(vcard_schema=None):  # noqa: E501
    """returns a qrcode that contains vcard data

     # noqa: E501

    :param vcard_schema: all the data of vcard in the qrcode
    :type vcard_schema: dict | bytes

    :rtype: SrcSchema
    """
    if connexion.request.is_json:
        vcard_schema = VcardSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return vcard_qrcode(vcard_schema)


def api_v1_qrcode_wifi_post(wifi_schema=None):  # noqa: E501
    """returns a qrcode that contains wifi credentials

     # noqa: E501

    :param wifi_schema: title and payload of the qrcode
    :type wifi_schema: dict | bytes

    :rtype: SrcSchema
    """
    if connexion.request.is_json:
        wifi_schema = WifiSchema.from_dict(connexion.request.get_json())  # noqa: E501
        wifi_schema = {
            "network": wifi_schema.network,
            "password": wifi_schema.password,
            "hiddenNetwork": wifi_schema.hidden_network if wifi_schema.hidden_network else False,
            "cryptage": wifi_schema.cryptage,
            "frame": wifi_schema.frame,
            "shape": wifi_schema.shape,
            "logo": wifi_schema.logo
        }
    return wifi_qrcode(wifi_schema)


def health_get():  # noqa: E501
    """returns ok if everything is alright

     # noqa: E501


    :rtype: InlineResponse200
    """
    return get_health()