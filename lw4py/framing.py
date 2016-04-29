from struct import pack, unpack
from lw4py.compat import py3k, ord, range

# Frame message type defined in the spec.
MTYPE_REQUEST = 0o0
MTYPE_ACCEPT = 0o1
MTYPE_UNCONFIRMED_DATA_UP = 0o2
MTYPE_UNCONFIRMED_DATA_DOWN = 0o3
MTYPE_CONFIRMED_DATA_UP = 0o4
MTYPE_CONFIRMED_DATA_DOWN = 0o5
MTYPE_REJOIN_REQUEST = 0o6
MTYPE_PROPRIETARY = 0o7


import gevent
from gevent import socket
urls= ['www.google.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=2)
print([job.value for job in jobs])
