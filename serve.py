__author__ = 'hadhya'

from gcm import GcmClient
from config import CONFIG
from optparse import OptionParser
import logging

def start_xmpp_server():
    client = GcmClient(CONFIG['GCM_API_KEY'])
    client.listen(CONFIG['GCM_SENDER_ID'], on_message)

def on_message(message):
    print message

if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)

    opts, args = optp.parse_args()

    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    start_xmpp_server()