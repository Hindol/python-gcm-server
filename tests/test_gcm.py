__author__ = 'hadhya'

from gcm import HttpMessage, GCMClient
import os

GCM_API_KEY = os.getenv('GCM_API_KEY', '')
GCM_SENDER_ID = os.getenv('GCM_SENDER_ID', '')

REGISTRATION_IDS = ['APA91bHxS-Os4gbKC0jyMEoz_xxJGieV6DhINeEoSIVJ0tzE4cRg7Ov8k9lJuhKJRtbY1EmwwOhXuIf8uj9WxIVnp-BajEv_ghJe348MTt396maff5QenTtIAImKmfeaCzagg-i19BEJdXvWhO0WwgSVOnrdSZsivsr9pUv33F2mwoMWHdf467w']

# A common payload used by many of the tests
def get_payload():
    payload = dict()
    payload['hello'] = 'world'
    return payload

def get_gcm_client():
    return GCMClient(GCM_API_KEY, GCM_SENDER_ID)

class TestHttpMessage:
    def test_wrap_unwrap(self):
        payload = get_payload()
        assert payload['hello'] == 'world'
        assert payload == HttpMessage(payload).get_payload()

class TestGcmClient:
    def test_send(self):
        payload = {'registration_ids': REGISTRATION_IDS, 'data': {'hello': 'world'}}
        print 'API key is ' + GCM_API_KEY
        gcm = get_gcm_client()
        res = gcm.send(0, payload)
        print res
        assert 1