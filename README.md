GCM Server Implementation in Python
===================================

A well documented idiomatic python implementation of a Google Cloud Messaging server.

Installation
------------

    pip install gcm-server (! Not yet active)

Usage
-----

### Send to Android Device ###

```python
from gcm import GCMClient

API_KEY = 'Your-API-key'
GCM_SENDER_ID = 'Your-Sender-ID'

gcm = GcmCLient(API_KEY)
payload = dict()
payload['registration_ids'] = ['1', '2', '3', ...]
payload['hello'] = 'world'

gcm.send(payload);
```

### Listen for Incoming Messages ###

```python
class Server:
	def __init__(self):
		gcm = GcmClient(API_KEY)
		gcm.listen(GCM_SENDER_ID, self.message_callback)

	def message_callback(self, message):
		# Do something with message
```
