# -*- coding: utf-8 -*-

import socket, errno
from contextlib import closing


def get_port(port=None):
    """
    Try fetching desided port.
    If it fails, ask system for a free one.
    """
    if port and port_available(port)[0]:
        return port
    else:
        return find_free_port()[0]


def port_available(port):
    """
    Check is port sent available currently.
    :return: {Tuple}
    """
    status = False
    error = {}
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        try:
            s.bind(('0.0.0.0', port))
            status = True
        except socket.error as e:
            # Most commonly expected to see: errno.EADDRINUSE
            error = {'errno': e.errno, 'msg': str(e)}

        return status, error


def find_free_port():
    """
    Ask the system for a free port.
    In case of error return error message.
    :return: {Tuple}
    """
    port = None
    error = {}
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        try:
            s.bind(('', 0))
            sock_name = s.getsockname()
            if type(sock_name) is tuple and len(sock_name) == 2:
                port = sock_name[1]
        except socket.error as e:
            error = {'errno': e.errno, 'msg': str(e)}

        return port, error
