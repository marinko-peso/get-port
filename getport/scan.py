# -*- coding: utf-8 -*-

import socket, errno
from contextlib import closing


def get_port(port):
    """
    Try fetching desided port.
    If it fails, ask system for a free one.
    """
    return None


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


if __name__ == '__main__':
    print(port_available(3306))
