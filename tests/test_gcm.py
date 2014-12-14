__author__ = 'hadhya'

from gcm import HttpMessage, GcmClient
import json
from config import CONFIG

# A common payload used by many of the tests
def get_payload():
    payload = dict()
    payload['hello'] = 'world'
    return payload

def get_gcm_client():
    return GcmClient(CONFIG['GCM_API_KEY'])

class TestHttpMessage:
    def test_wrap_unwrap(self):
        payload = get_payload()
        assert payload['hello'] == 'world'
        assert payload == HttpMessage(payload).get_payload()

class TestGcmClient:
    def test_send(self):
        payload = {'registration_ids': CONFIG['REGISTRATION_IDS'], 'data': {'hello': 'world'}}
        gcm = get_gcm_client()
        print gcm.https_header
        res = json.loads(gcm.send(payload))
        assert res['failure'] == 0

    def test_listen(self):
        gcm = get_gcm_client()
        gcm.listen(CONFIG['GCM_SENDER_ID'], self.on_message)

    def on_message(self, message):
        print message