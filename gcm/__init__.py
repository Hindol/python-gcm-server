__author__ = 'hadhya'

from abc import ABCMeta, abstractmethod
from string import Template
import urllib2
import json

GCM_HTTP_SERVER_URL = 'https://android.googleapis.com/gcm/send'

# HTTP message standard header
HTTPS_HEADER = {
    'Content-Type': 'application/json',
    'Authorization': Template('key=$api_key')
}

class Message:
    """
    A message class to ease the construction and parsing of GCM payload.
    """
    __metaclass__ = ABCMeta

    def __init__(self, payload):
        self.payload = payload

    def get_payload(self):
        return self.payload

class XmppMessage(Message):
    """
    Models the XMPP message type for GCM.
    """

    def __init__(self, payload):
        Message.__init__(self, payload)

class HttpMessage(Message):
    """
    Models the HTTP message type for GCM.
    """

    def __init__(self, payload):
        Message.__init__(self, payload)

class GCMClient:
    def __init__(self, api_key, sender_id=None):
        self.api_key = api_key
        self.sender_id = sender_id

        self.https_url = GCM_HTTP_SERVER_URL
        self.https_header = HTTPS_HEADER
        self.https_header['Authorization'] = self.https_header['Authorization'].substitute(api_key=self.api_key)

    def send(self, msg_id, payload=None, ttl=240):
        payload = json.dumps(payload)
        req = urllib2.Request(self.https_url, payload, self.https_header)
        res = urllib2.urlopen(req).read()

        return res