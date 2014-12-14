__author__ = 'hadhya'

import os

CONFIG = {
    'GCM_HTTPS_SERVER_URL': 'https://android.googleapis.com/gcm/send',
    'GCM_XMPP_SERVER_URL': 'gcm.googleapis.com',
    'GCM_XMPP_SERVER_PORT': 5235,

    'GCM_API_KEY': os.getenv('GCM_API_KEY'),
    'GCM_SENDER_ID': os.getenv('GCM_SENDER_ID'),

    'REGISTRATION_IDS': [
        'APA91bHxS-Os4gbKC0jyMEoz_xxJGieV6DhINeEoSIVJ0tzE4cRg7Ov8k9lJuhKJRtbY1EmwwOhXuIf8uj9WxIVnp-BajEv_ghJe348MTt396maff5QenTtIAImKmfeaCzagg-i19BEJdXvWhO0WwgSVOnrdSZsivsr9pUv33F2mwoMWHdf467w']
}