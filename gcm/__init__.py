__author__ = 'hadhya'

from abc import ABCMeta
from string import Template
import urllib2
import json
import sleekxmpp
import logging
from copy import deepcopy
from config import CONFIG

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


class _GcmXmppClient(sleekxmpp.ClientXMPP):
    def __init__(self, api_key, sender_id):
        super(_GcmXmppClient, self).__init__(sender_id, api_key)


class GcmClient:
    def __init__(self, api_key):
        self.api_key = api_key

        # Configure HTTP
        self.https_url = CONFIG['GCM_HTTPS_SERVER_URL']
        self.https_header = deepcopy(HTTPS_HEADER)
        self.https_header['Authorization'] = self.https_header['Authorization'].substitute(api_key=self.api_key)

    def send(self, payload=None):
        payload = json.dumps(payload)
        req = urllib2.Request(self.https_url, payload, self.https_header)
        res = urllib2.urlopen(req).read()

        return res

    def listen(self, sender_id, message_callback):
        print 'Hello Gandu'
        # If sender id is given, also instantiate an xmpp client
        if not sender_id:
            logging.error('Sender ID not specified. Cannot start XMPP listen server.')
            return

        if not message_callback:
            logging.error('Please specify a message callback.')
            return

        self.xmpp_client = _GcmXmppClient(self.api_key, sender_id)
        self.xmpp_client.add_event_handler('message', message_callback)

        if self.xmpp_client.connect((CONFIG['GCM_XMPP_SERVER_URL'], CONFIG['GCM_XMPP_SERVER_PORT']), use_ssl=True):
            logging.info('Connected to XMPP server.')
            self.xmpp_client.process()
        else:
            logging.error('Could not connect to XMPP server.')
            return
