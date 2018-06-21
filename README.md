# Sites Monitoring Utility

Utility for checking the status of sites.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Example of script launch on Linux and Windows, Python 3.5:

```bash
$ python check_sites_health.py filepath
```

```bash
Required parameters:
filepath - Path to a file with a list of URLs
```

The program displays result of checking in the console:

```bash
URL: https://devman.org
Good! Status code: 200
Good! Until the expiry date is more than a month.

URL: http://dsfsdf.ru
Seems like dns lookup failed.
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
