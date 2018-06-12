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

The program displays the URL, status code, expiration date and errors in the console:

```bash
URL: https://devman.org
Status code: 200
Expiration date: 2018-08-28 11:49:42

URL: https://yandex.ru
Status code: 200
Expiration date: 2018-09-30 21:00:00

URL: http://dsfsdf.ru
Seems like dns lookup failed.
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
