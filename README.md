GCM Server Implementation in Python
===================================

A well documented idiomatic python implementation of a Google Cloud Messaging server.

Installation
------------

    pip install gcm-server

Usage
-----

```python
from gcm import GCMClient

API_KEY = 'Your-API-key'
GCM_SENDER_ID = 'Your-Sender-ID'

gcm = GCMCLient(API_KEY)
msg_id = 0;
id = msg_id++
data = dict()
data['hello'] = 'world'

gcm.send(sender_id=GCM_SENDER_ID + "@gcm.googleapis.com", msg_id=id, ttl=600, data);
```