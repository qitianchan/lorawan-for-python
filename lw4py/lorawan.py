import logging
import socket
import threading

logger = logging.getLogger('lrw4py')

class LoRaWan(object):
    def __init__(self, sock, type, major=None, heartbeat_freq=None, network_id=None):
       self.sock = sock

    def received_message(self, message):
        """
        Called whenever a complete ``message``,
        is received and ready for application's processing.

        .. note:: You should override this method in your subclass.
        """
        pass

    def unhandled_error(self, error):
        logger.exception('Failed to receive data')
