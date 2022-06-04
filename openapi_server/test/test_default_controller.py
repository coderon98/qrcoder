# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.email_schema import EmailSchema  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.sms_schema import SmsSchema  # noqa: E501
from openapi_server.models.src_schema import SrcSchema  # noqa: E501
from openapi_server.models.text_schema import TextSchema  # noqa: E501
from openapi_server.models.url_schema import UrlSchema  # noqa: E501
from openapi_server.models.vcard_schema import VcardSchema  # noqa: E501
from openapi_server.models.wifi_schema import WifiSchema  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_api_v1_qrcode_email_post(self):
        """Test case for api_v1_qrcode_email_post

        returns a qrcode that contains email data
        """
        email_schema = openapi_server.EmailSchema()
        headers = { 
            'Accept': 'image/png',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/qrcode/email',
            method='POST',
            headers=headers,
            data=json.dumps(email_schema),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_qrcode_sms_post(self):
        """Test case for api_v1_qrcode_sms_post

        returns a qrcode that contains sms credentials
        """
        sms_schema = openapi_server.SmsSchema()
        headers = { 
            'Accept': 'image/png',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/qrcode/sms',
            method='POST',
            headers=headers,
            data=json.dumps(sms_schema),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_qrcode_text_post(self):
        """Test case for api_v1_qrcode_text_post

        returns a qrcode that contains simple text (500 characters maximum)
        """
        text_schema = openapi_server.TextSchema()
        headers = { 
            'Accept': 'image/png',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/qrcode/text',
            method='POST',
            headers=headers,
            data=json.dumps(text_schema),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_qrcode_url_post(self):
        """Test case for api_v1_qrcode_url_post

        returns a qrcode that contains url data
        """
        url_schema = openapi_server.UrlSchema()
        headers = { 
            'Accept': 'image/png',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/qrcode/url',
            method='POST',
            headers=headers,
            data=json.dumps(url_schema),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_qrcode_vcard_post(self):
        """Test case for api_v1_qrcode_vcard_post

        returns a qrcode that contains vcard data
        """
        vcard_schema = openapi_server.VcardSchema()
        headers = { 
            'Accept': 'image/png',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/qrcode/vcard',
            method='POST',
            headers=headers,
            data=json.dumps(vcard_schema),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_qrcode_wifi_post(self):
        """Test case for api_v1_qrcode_wifi_post

        returns a qrcode that contains wifi credentials
        """
        wifi_schema = openapi_server.WifiSchema()
        headers = { 
            'Accept': 'image/png',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/qrcode/wifi',
            method='POST',
            headers=headers,
            data=json.dumps(wifi_schema),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_health_get(self):
        """Test case for health_get

        returns ok if everything is alright
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/health',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
