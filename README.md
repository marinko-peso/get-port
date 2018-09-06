# get-port
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![license](https://img.shields.io/github/license/marinko-peso/get-port.svg)](https://github.com/marinko-peso/get-port/blob/master/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/marinko-peso/get-port.svg?maxAge=3600)](https://github.com/marinko-peso/get-port/commits/master)
[![PyPI](https://img.shields.io/pypi/v/get-port.svg)](https://pypi.org/project/get-port/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/get-port.svg)](https://pypi.org/project/get-port/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Get an available port. Checks first for preferred port in case its available, if not returns random.
Python implementation of the [get-port](https://github.com/sindresorhus/get-port) idea by @[sindresorhus](https://github.com/sindresorhus/).


## Installation.

Available via PyPI.
```sh
pip install get-port
```


## Usage.

Available in terminal:
```sh
get-port [preferred-port-optional]
```

Usage in code:
```python
# Gets the actual port. Send preferred_port to pick if available.
from get_port import get_port
port = get_port(preferred_port)

# Check if port is available. Returns tuple: (Boolean, Dict)
from get_port import port_available
is_available = port_available(your_port)

# Find random free port. Returns tuple: (Port, Dict)
from get_port import find_free_port
port = find_free_port()
```


## License

MIT.
