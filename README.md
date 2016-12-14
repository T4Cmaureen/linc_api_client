# LINC API Client - An HTTP Python Client to [LINC API](https://github.com/linc-lion/linc-api)

![GitHub Release](https://img.shields.io/badge/release-v0.0.1-blue.svg)
![GitHub license](https://img.shields.io/badge/license-GPLv3-yellow.svg)

The LINC API Client is a python package that handles HTTP calls with the LINC API.

## Table of contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Example of use](#exampleofuse)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [Maintainers](#maintainers)
* [License](#license)

## Requirements

* python 3.5+ => the version used in the package development and also testing.
* requests
* certifi (to avoid SSL/HTTPS error in requests package)

## Installation

### Using PIP

We present here an installation with a **virtualenv** (requires ssh keys configured in the BitBucket user profile):

```
$ virtualenv --python=python3.5 --prompt=" <LINC API Client> " venv-3.5
$ source venv-3.5/bin/activate ; pip install --upgrade pip setuptools
 <LINC API Client> $ pip install git+
 <LINC API Client> $ pip list
 linc-api-client (0.0.1)
 pip (9.0.1)
 requests (2.12.3)
 setuptools (30.2.0)
 wheel (0.26.0)
 ```

### For Development

In order to install the LINC API Client application, follow the steps:

```
$ cd <repo>
$ mkdir tests
$ cd tests
$ virtualenv --python=python3.5 --prompt=" <package name> " venv-3.5
$ source venv-3.5/bin/activate
$ pip install pip setuptools --upgrade
$ cd .. ; python setup.py install ; cd -
```

## Example of use

```python
# Execute this to see logging info
import logging,sys
root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

from linc_api_client import Connection
c = Connection('localhost',9090)

```

## Troubleshooting

If you are using Ubuntu, you may face the following error when installing the linc_api_client package over Python 3.5:
```
gevent/gevent.corecext.c:5:20: fatal error: Python.h: No such file or directory
```
To solve this problem, just install the `python3-dev` package on your machine and try installing linc_api_client again.

## Contributing

Fork the repository and do a pull request.
Please file a github issue to [report a bug]().

## Maintainers

[Venidera Research and Development](http://portal.venidera.com) team:

* Andre E. Toscano - [andre@venidera.com](mailto:andre@venidera.com)

## License

This package is released and distributed under the license [GNU GPL Version 3, 29 June 2007](https://www.gnu.org/licenses/gpl-3.0.html).
